import os 
import bcrypt
import pyotp
import pwnedpasswords
from cryptography.fernet import Fernet
#  The function generates an encryption key and saves it in a file called secret.key.
def generate_key():
  key = fernet.generate_key()
  with open("secret_file", "wb") as key_file:
    key_file.write(key)
def load_key():
  Return open("secret_file", "rb").read()
  def encrypt_password(password):
    key =load_key()
    fernet =  fernet(key)
    







