def is_adult(citizen_details):
    age = citizen_details.get('age')
    return age is not None and age >= 18

if __name__ == '__main__':
    sample_citizen = {'name': 'Alice', 'age': 25}
    result = is_adult(sample_citizen)
    print(result)