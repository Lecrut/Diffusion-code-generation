def check_key_presence(data: dict) -> list:
    return [key for key in data.keys() if isinstance(key, str)]
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20, 'cherry': 30}
    result = check_key_presence(sample_data)
    print(result)