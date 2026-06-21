def is_adult(citizen_details):
    return citizen_details.get('age', None) is not None and citizen_details['age'] >= 18

if __name__ == '__main__':
    print(is_adult({'age': 20}))
    print(is_adult({'age': 17}))
    print(is_adult({}))
    print(is_adult({'name': 'Alice'}))
    print(is_adult({'age': 18}))
    print(is_adult({'age': 0}))
    print(is_adult({'age': -5}))