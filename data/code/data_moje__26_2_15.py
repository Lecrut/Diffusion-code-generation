def check_adult(citizen_details):
    if 'age' not in citizen_details:
        return False
    try:
        return int(citizen_details['age']) >= 18
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    sample_data_1 = {'name': 'Alice', 'age': '25'}
    sample_data_2 = {'name': 'Bob', 'age': '15'}
    sample_data_3 = {'name': 'Charlie'}
    print(check_adult(sample_data_1))
    print(check_adult(sample_data_2))
    print(check_adult(sample_data_3))