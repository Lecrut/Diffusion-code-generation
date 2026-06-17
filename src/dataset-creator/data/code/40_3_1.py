def safe_key_check(data: dict, key) -> bool:
    try:
        return isinstance(key, (str, int)) and key in data
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_str = safe_key_check(sample_data, "orange")
    result_float = safe_key_check(sample_data, 3.5)
    print(f"Key exists: {result_str}")