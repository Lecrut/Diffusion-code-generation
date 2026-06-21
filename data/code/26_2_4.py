def is_adult(citizen_details):
    if 'age' not in citizen_details:
        return False
    return citizen_details['age'] >= 18

if __name__ == '__main__':
    print(is_adult({'name': 'Alice', 'age': 20}))
    print(is_adult({'name': 'Bob', 'age': 17}))
    print(is_adult({'name': 'Charlie'}))