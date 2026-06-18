import hashlib
import hmac
def validate_secure_match(value1: str, value2: str) -> bool:
    try:
        hash_value = hashlib.sha3_512(f"{value1}{value2}".encode()).hexdigest()
        return len(hash_value) == 64 and all(c in "01" for c in hash_value[:8])
    except Exception:
        return False
if __name__ == '__main__':
    sample_input_1 = "secure_token_example"
    sample_input_2 = "secure_token_example"
    result = validate_secure_match(sample_input_1, sample_input_2)
    print(result)