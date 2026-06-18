import hashlib
import hmac
def constant_time_compare(a: bytes, b: bytes) -> bool:
    return hmac.compare_digest(a, b)
if __name__ == '__main__':
    str1 = "secure_string_example"
    str2 = "secure_string_example"
    hash1 = hashlib.sha256(str1.encode()).digest()
    hash2 = hashlib.sha256(str2.encode()).digest()
    result = constant_time_compare(hash1, hash2)
    print(result)