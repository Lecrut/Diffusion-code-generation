import hashlib
import hmac
from typing import Tuple
def secure_hash_compare(a: bytes, b: bytes) -> bool:
    return hmac.compare_digest(a, b)
if __name__ == '__main__':
    sample_str_1 = "secret_message"
    sample_str_2 = "different_content"
    hash_algo = hashlib.sha512
    h1 = hash_algo(sample_str_1.encode()).digest()
    h2 = hash_algo(sample_str_2.encode()).digest()
    result = secure_hash_compare(h1, h2)
    print(result)