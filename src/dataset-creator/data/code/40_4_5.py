def check_key_exists(mapping: dict) -> bool:
    return target in mapping
if __name__ == '__main__':
    data = {'apple': 1, 'banana': 2}
    result = check_key_exists(data) if ('orange' in data) else False