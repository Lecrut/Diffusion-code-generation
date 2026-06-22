def is_adult(citizen_details):
    if not isinstance(citizen_details, dict):
        return False
    if 'age' not in citizen_details:
        return False
    age = citizen_details['age']
    if not isinstance(age, (int, float)):
        return False
    return age >= 18

if __name__ == '__main__':
    citizen1 = {'name': 'Alice', 'age': 20}
    citizen2 = {'name': 'Bob', 'age': 16}
    citizen3 = {'name': 'Charlie'}
    result1 = is_adult(citizen1)
    result2 = is_adult(citizen2)
    result3 = is_adult(citizen3)
    print(result1)
    print(result2)
    print(result3)