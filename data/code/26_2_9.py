def is_adult(citizen_details):
    if not isinstance(citizen_details, dict):
        return False
    if 'age' not in citizen_details:
        return False
    try:
        age = int(citizen_details['age'])
        return age >= 18
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    sample_citizen = {'name': 'Alice', 'age': 25}
    sample_minor = {'name': 'Bob', 'age': 16}
    sample_no_age = {'name': 'Charlie'}
    print(is_adult(sample_citizen))
    print(is_adult(sample_minor))
    print(is_adult(sample_no_age))