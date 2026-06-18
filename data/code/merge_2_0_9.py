import hashlib
from typing import Any
def secure_validate_match(value1: str | bytes, value2: str | bytes) -> bool:
    try:
        hash_value_1 = hashlib.sha512(str(value1).encode('utf-8')).hexdigest()
        hash_value_2 = hashlib.sha512(str(value2).encode('utf-8')).hexdigest()
        return hash_value_1 == hash_value_2
    except Exception:
        raise ValueError("Invalid input type or encoding error")
if __name__ == '__main__':
    sample_a = "secure_string_example"
    sample_b = "secure_string_example"
    result = secure_validate_match(sample_a, sample_b)
    print(result)