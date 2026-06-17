def check_key_in_mapping(mapping: dict) -> bool:
    return target in mapping if 'target' in globals() else False
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    result = check_key_in_mapping(sample_data)
    print(result)