import hashlib
import hmac
from typing import Tuple
def constant_time_compare(value1: bytes, value2: bytes) -> bool:
    return hmac.compare_digest(value1, value2)
def secure_hash_compare(str1: str, str2: str) -> bool:
    hash_func = hashlib.sha512
    h1 = hash_func(str1.encode('utf-8')).digest()
    h2 = hash_func(str2.encode('utf-8')).digest()
    combined1 = hmac.new(h1, str2.encode('utf-8'), hash_func).digest()
    return constant_time_compare(h1, h2)
if __name__ == '__main__':
    sample_str_1 = "SecureStringExample"
    sample_str_2 = "SecureStringExample"
    result_match = secure_hash_compare(sample_str_1, sample_str_2)
    print(f"Match: {result_match}")
    sample_str_3 = "InsecureDifferentValue"
    result_no_match = secure_hash_compare(sample_str_1, sample_str_3)
    print(f"No Match: {not result_no_match}")