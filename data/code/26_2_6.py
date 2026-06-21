def check_age(citizen_details):
    if 'age' not in citizen_details:
        return False
    return citizen_details['age'] >= 18

if __name__ == '__main__':
    sample_citizen = {'name': 'Alice', 'age': 20}
    result = check_age(sample_citizen)
    print(result)