def check_key_exists(mapping: dict, target: str) -> bool:
    return target in mapping
if __name__ == '__main__':
    data = {'apple': 10, 'banana': 20, 'cherry': 30}
    print(check_key_exists(data, 'banana'))