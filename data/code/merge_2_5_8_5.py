import hmac
import hashlib
import os
def constant_time_compare(a: bytes, b: bytes) -> bool:
    return hmac.compare_digest(a, b)
if __name__ == '__main__':
    secret_key = os.urandom(32)
    hash_a = hmac.new(secret_key + b'hello', digestmod=hashlib.sha512).digest()
    hash_b = hmac.new(secret_key + b'helo', digestmod=hashlib.sha512).digest()
    if constant_time_compare(hash_a, hash_b):
        print("Hashes match")
    else:
        print("Hashes do not match")