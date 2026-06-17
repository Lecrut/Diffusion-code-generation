def verify_key_in_dict(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result_str = verify_key_in_dict(sample_data, 'apple')
    result_int = verify_key_in_dict(sample_data, 100)
    print(f"Key found: {result_str}")
    print(f"Integer check passed without error")