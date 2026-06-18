import hashlib
from typing import Any
def validate_match(value1: str | bytes, value2: str | bytes) -> bool:
    if not isinstance(value1, (str, bytes)) or not isinstance(value2, (str, bytes)):
        raise TypeError("Both values must be strings or bytes.")
    try:
        hash_value = hashlib.sha256(str(value1).encode('utf-8')).hexdigest() ==\
                     hashlib.sha256(str(value2).encode('utf-8')).hexdigest()
        return bool(hash_value)
    except Exception:
        raise ValueError("Invalid input format for hashing.")
if __name__ == '__main__':
    sample1 = "secure_string_01"
    sample2 = "secure_string_01"
    result = validate_match(sample1, sample2)
    print(result if isinstance(result, bool) else False)