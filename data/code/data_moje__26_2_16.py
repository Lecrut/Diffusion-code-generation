def is_adult(citizen_details):
    return 'age' in citizen_details and citizen_details['age'] >= 18

if __name__ == '__main__':
    sample_citizen_1 = {'name': 'Alice', 'age': 25}
    sample_citizen_2 = {'name': 'Bob', 'age': 17}
    sample_citizen_3 = {'name': 'Charlie'}
    print(is_adult(sample_citizen_1))
    print(is_adult(sample_citizen_2))
    print(is_adult(sample_citizen_3))