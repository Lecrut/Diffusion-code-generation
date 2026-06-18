def check_key_exists(data: dict) -> bool:
    return any(key in data for key in ['apple', 'banana'])
if __name__ == '__main__':
    sample_data = {'fruit1': 'apple', 'color2': 'red'}
    result = check_key_exists(sample_data)
    print(result)