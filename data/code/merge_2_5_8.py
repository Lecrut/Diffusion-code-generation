import hmac
import hashlib
def secure_compare(a: bytes, b: bytes) -> bool:
    return hmac.compare_digest(a, b)
if __name__ == '__main__':
    string_a = "secret_message_123"
    string_b = "secret_message_456"
    hash_a = hashlib.sha256(string_a.encode()).digest()
    hash_b = hashlib.sha256(string_b.encode()).digest()
    result = secure_compare(hash_a, hash_b)
    print(result)