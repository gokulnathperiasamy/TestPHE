# pip3 install lightphe

from lightphe import LightPHE
from lightphe.cryptosystems.RSA import RSA

phe = LightPHE(algorithm_name="Paillier")
rsa = RSA()
rsa_lite = LightPHE(algorithm_name="RSA")

def add_two_numbers(v1, v2):
    # Encrypt the input values
    c1 = phe.encrypt(v1)
    c2 = phe.encrypt(v2)    
    
    c3 = c1 + c2
    
    print("Adding Two Numbers: ", v1, v2)
    print("Decrypted result:", phe.decrypt(c3))

def integer_multiplication(v1, v2):
    # Encrypt the input values
    c1 = rsa.encrypt(v1)
    c2 = rsa.encrypt(v2)

    c3 = rsa.multiply(c1, c2)
    
    print("Integer Multiplication: ", v1, v2)
    print("Decrypted result:", rsa.decrypt(c3))

def float_multiplication(v1, v2):
    c1 = rsa_lite.encrypt(plaintext=v1)
    c2 = rsa_lite.encrypt(plaintext=v2)
    
    c3 = c1 * c2

    print("Float Multiplication: ", v1, v2)
    print("Decrypted result:", rsa_lite.decrypt(c3))

print("------------------- ******************** -------------------")
add_two_numbers(95, -91)
print("------------------- ******************** -------------------")
integer_multiplication(45, 5)
print("------------------- ******************** -------------------")
float_multiplication(3500000, 12.50)
print("------------------- ******************** -------------------")