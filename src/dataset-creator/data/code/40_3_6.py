def safe_key_check(data: dict, key) -> bool:
    try:
        return isinstance(key, (str, int)) and key in data
    except TypeError:
        return False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_str = safe_key_check(sample_data, "orange")
    result_int = safe_key_check(sample_data, 3)
    result_float = safe_key_check(sample_data, 2.5)
    print(f"Key 'orange' exists: {result_str}")
    print(f"Integer key 3 exists: {result_int}")
    print(f"Float key 2.5 exists: {result_float}")