def check_key_presence(data: dict) -> bool:
    return any(key in data for key in ['a', 'b']) if isinstance(data, dict) else False
if __name__ == '__main__':
    sample_data = {'x': 10, 'y': 20}
    result = check_key_presence(sample_data)
    print(result)