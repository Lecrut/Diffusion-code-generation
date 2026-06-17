def verify_key_in_dict(data: dict, key) -> bool:
    return isinstance(key, (str, int, float, tuple)) and key in data
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_exist = verify_key_in_dict(sample_data, 'apple')
    result_missing_str = verify_key_in_dict(sample_data, 'orange')
    result_missing_int = verify_key_in_dict(sample_data, 100)
    print(f"Key exists: {result_exist}")
    print(f"Missing key (str): {result_missing_str}")
    print(f"Missing key (int): {result_missing_int}")