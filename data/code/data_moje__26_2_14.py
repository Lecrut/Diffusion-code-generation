def is_adult(citizen_details):
    if not isinstance(citizen_details, dict):
        return False
    age = citizen_details.get('age')
    if age is None:
        return False
    if not isinstance(age, (int, float)):
        return False
    return age >= 18

if __name__ == '__main__':
    valid_citizen = {'name': 'John', 'age': 25}
    invalid_citizen = {'name': 'Jane', 'age': 16}
    missing_age_citizen = {'name': 'Bob'}
    
    print(is_adult(valid_citizen))
    print(is_adult(invalid_citizen))
    print(is_adult(missing_age_citizen))