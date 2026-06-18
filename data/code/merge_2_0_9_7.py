import hashlib
from typing import Any
def secure_validate_match(value1: str | bytes, value2: str | bytes) -> bool:
    if not isinstance(value1, (str, bytes)) or not isinstance(value2, (str, bytes)):
        raise TypeError("Both values must be strings or bytes.")
    try:
        hash_value_1 = hashlib.sha256(str(value1).encode('utf-8')).hexdigest()
        hash_value_2 = hashlib.sha256(str(value2).encode('utf-8')).hexdigest()
        return hash_value_1 == hash_value_2
    except Exception:
        raise ValueError("Invalid input format for hashing.")
if __name__ == '__main__':
    sample_input_a = "secure_string"
    sample_input_b = "another_secure_string"
    result = secure_validate_match(sample_input_a, sample_input_b)
    if result:
        print("Values match exactly.")
    else:
        print("Values do not match.")