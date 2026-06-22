def check_adult(citizen_details):
    if 'age' not in citizen_details:
        return False
    return citizen_details['age'] >= 18

if __name__ == '__main__':
    print(check_adult({'name': 'Alice', 'age': 20}))
    print(check_adult({'name': 'Bob', 'age': 17}))
    print(check_adult({'name': 'Charlie'}))
    print(check_adult({'name': 'David', 'age': 18}))