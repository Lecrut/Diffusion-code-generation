import hashlib
import hmac
from typing import Tuple
def constant_time_compare(value1: bytes, value2: bytes) -> bool:
    return hmac.compare_digest(value1, value2)
if __name__ == '__main__':
    sample_string_1 = "secure_password_hash_example"
    sample_string_2 = "secure_password_hash_example"
    hash_algorithm = hashlib.sha512
    hashed_value_1 = hash_algorithm(sample_string_1.encode('utf-8')).digest()
    hashed_value_2 = hash_algorithm(sample_string_2.encode('utf-8')).digest()
    comparison_result = constant_time_compare(hashed_value_1, hashed_value_2)
    print(f"Hashes match: {comparison_result}")