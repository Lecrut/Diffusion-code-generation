import hashlib
def validate_match(value1: str | bytes, value2: str | bytes) -> bool:
    try:
        if isinstance(value1, str):
            hash_value_1 = hashlib.sha256(value1.encode('utf-8')).hexdigest()
        else:
            hash_value_1 = hashlib.sha256(bytes()).hexdigest()
        if isinstance(value2, str):
            hash_value_2 = hashlib.sha256(value2.encode('utf-8')).hexdigest()
        else:
            hash_value_2 = hashlib.sha256(bytes()).hexdigest()
        return hash_value_1 == hash_value_2 and value1 != '' and value2 != ''
    except Exception:
        return False
if __name__ == '__main__':
    sample_a = "secure_string"
    sample_b = "secure_string"
    result = validate_match(sample_a, sample_b)
    print(result)