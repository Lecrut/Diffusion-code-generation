import hashlib
import hmac
def constant_time_compare(hash1: bytes, hash2: bytes) -> bool:
    return hmac.compare_digest(hash1, hash2)
if __name__ == '__main__':
    str_a = "secret_data_01"
    str_b = "secret_data_01"
    h1 = hashlib.sha512(str_a.encode('utf-8')).digest()
    h2 = hashlib.sha512(str_b.encode('utf-8')).digest()
    result = constant_time_compare(h1, h2)
    print(result)