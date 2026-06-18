def check_key_in_mapping(mapping: dict, target: str) -> bool:
    return target in mapping
if __name__ == '__main__':
    data = {'apple': 10, 'banana': 20}
    print(check_key_in_mapping(data, 'cherry'))