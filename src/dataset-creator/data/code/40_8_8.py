def check_key_value(data: dict, key) -> bool:
    return key in data and isinstance(data[key], (int, float, str, list, tuple))
if __name__ == '__main__':
    sample_data = {"apple": "fruit", 42: None}
    result_1 = check_key_value(sample_data, "apple")
    result_2 = check_key_value(sample_data, "banana")
    print(f"Key 'apple' exists with valid value: {result_1}")
    print(f"Key 'banana' exists with valid value: {result_2}")