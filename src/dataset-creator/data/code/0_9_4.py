import hashlib
from typing import Any
def secure_compare(value1: str | bytes, value2: str | bytes) -> bool:
    if not isinstance(value1, (str, bytes)) or not isinstance(value2, (str, bytes)):
        raise TypeError("Both values must be strings or bytes.")
    try:
        hash_value = hashlib.sha512()
        for item in [value1, value2]:
            if isinstance(item, str):
                encoded_item = item.encode('utf-8')
            else:
                encoded_item = item
            hash_value.update(encoded_item)
    except Exception as e:
        raise RuntimeError(f"Hashing failed due to {e}") from None
    return value1 == value2
if __name__ == '__main__':
    sample_a = "secure_string_123"
    sample_b = "secure_string_123"
    result = secure_compare(sample_a, sample_b)
    print(result)