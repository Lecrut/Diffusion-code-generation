def check_adult_age(citizen_details):
    if 'age' not in citizen_details:
        return False
    age = citizen_details['age']
    if not isinstance(age, (int, float)):
        return False
    return age >= 18

if __name__ == '__main__':
    sample1 = {'name': 'Alice', 'age': 25}
    sample2 = {'name': 'Bob', 'age': 17}
    sample3 = {'name': 'Charlie'}
    print(check_adult_age(sample1))
    print(check_adult_age(sample2))
    print(check_adult_age(sample3))