import hashlib
from typing import Any
def secure_validate_match(value1: str, value2: str) -> bool:
    try:
        hash1 = hashlib.sha256(value1.encode('utf-8')).hexdigest()
        hash2 = hashlib.sha256(value2.encode('utf-8')).hexdigest()
        return hash1 == hash2
    except Exception:
        return False
if __name__ == '__main__':
    sample_value_1 = "secure_string_example"
    sample_value_2 = "secure_string_example"
    result = secure_validate_match(sample_value_1, sample_value_2)
    print(result if isinstance(result, bool) else f"{result}")