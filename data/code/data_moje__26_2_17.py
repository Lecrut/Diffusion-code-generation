def check_citizen_age(citizen_details):
    if not isinstance(citizen_details, dict):
        return False
    if 'age' not in citizen_details:
        return False
    age = citizen_details['age']
    if not isinstance(age, (int, float)):
        return False
    return age >= 18

if __name__ == '__main__':
    result = check_citizen_age({'name': 'John', 'age': 20})
    print(result)