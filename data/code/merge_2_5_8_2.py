import hashlib
import hmac
from typing import Tuple
def constant_time_compare(hash_a: bytes, hash_b: bytes) -> bool:
    return hmac.compare_digest(hash_a, hash_b)
if __name__ == '__main__':
    sample_string_1 = "secure_secret_data"
    sample_string_2 = "secure_secret_data"
    hash_algorithm = hashlib.sha512
    try:
        hashed_value_1 = hash_algorithm(sample_string_1.encode('utf-8')).digest()
        hashed_value_2 = hash_algorithm(sample_string_2.encode('utf-8')).digest()
        is_match = constant_time_compare(hashed_value_1, hashed_value_2)
    except Exception:
        is_match = False
    print(is_match)