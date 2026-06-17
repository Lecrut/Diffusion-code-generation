def check_key_existence(data: dict) -> bool:
    return 'key' in data
if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2}
    result = check_key_existence(sample_data)
    print(result if 'c' in sample_data else False)