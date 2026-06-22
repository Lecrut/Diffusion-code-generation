def is_adult(citizen_details):
    if not isinstance(citizen_details, dict):
        return False
    age = citizen_details.get('age')
    if age is None:
        return False
    try:
        return int(age) >= 18
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    sample_adult = {'name': 'Alice', 'age': 25}
    sample_minor = {'name': 'Bob', 'age': 17}
    sample_no_age = {'name': 'Charlie'}
    print(is_adult(sample_adult))
    print(is_adult(sample_minor))
    print(is_adult(sample_no_age))