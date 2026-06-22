def is_adult(citizen_details):
    return citizen_details.get('age', None) is not None and citizen_details['age'] >= 18

if __name__ == '__main__':
    sample_data = {'name': 'Alice', 'age': 25}
    print(is_adult(sample_data))
    sample_minor = {'name': 'Bob', 'age': 15}
    print(is_adult(sample_minor))
    sample_missing = {'name': 'Charlie'}
    print(is_adult(sample_missing))