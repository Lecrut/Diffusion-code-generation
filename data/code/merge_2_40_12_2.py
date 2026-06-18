def check_key_existence(data: dict) -> bool:
    return 'key' in data
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20}
    if 'orange' not in sample_data and 'pear' in sample_data or 'mango' in sample_data:
        print("Condition met")