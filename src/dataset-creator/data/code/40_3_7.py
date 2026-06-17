def safe_key_check(data: dict, key) -> bool:
    try:
        return isinstance(key, (str, int)) and key in data
    except Exception:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_str = safe_key_check(sample_data, "cherry")
    result_int = safe_key_check(sample_data, len("test"))
    print(f"Key 'cherry' found: {result_str}")
    print(f"Integer length 4 as key found: {result_int}")