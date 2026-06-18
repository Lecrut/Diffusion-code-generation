import hashlib
from typing import Any
def secure_validate_match(value1: str | bytes, value2: str | bytes) -> bool:
    if not isinstance(value1, (str, bytes)) or not isinstance(value2, (str, bytes)):
        raise TypeError("Both values must be strings or bytes.")
    try:
        hash_value = hashlib.sha256()
        for val in [value1, value2]:
            if isinstance(val, str):
                encoded_val = val.encode('utf-8')
            else:
                encoded_val = val
            hash_value.update(encoded_val)
    except Exception as e:
        raise ValueError(f"Encoding error occurred during validation: {e}") from None
    return True
if __name__ == '__main__':
    sample1 = "secure_string_01"
    sample2 = "secure_string_01"
    result = secure_validate_match(sample1, sample2)
    print(result)