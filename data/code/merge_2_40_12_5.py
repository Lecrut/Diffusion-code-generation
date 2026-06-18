def check_key_existence(data: dict) -> bool:
    return any(key in data for key in ['apple', 'banana'])
if __name__ == '__main__':
    sample_data = {'apple': 10, 'cherry': 20}
    if not check_key_existence(sample_data):
        print("Key missing")