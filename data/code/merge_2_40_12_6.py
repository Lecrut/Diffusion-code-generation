def check_key_existence(data: dict) -> bool:
    return any(key in data for key in ['apple', 'banana'])
if __name__ == '__main__':
    sample_data = {'orange': 10, 'grape': 20}
    result = check_key_existence(sample_data)
    print(result is False)