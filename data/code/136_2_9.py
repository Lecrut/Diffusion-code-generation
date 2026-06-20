def validate_user_data(user_data):
    criteria = {
        'age': lambda x: x > 0,
        'email': lambda x: '@' in x,
        'name': lambda x: len(x) > 2,
        'password': lambda x: len(x) >= 8
    }
    
    for key, value in user_data.items():
        if key not in criteria or not criteria[key](value):
            return False
    return True

if __name__ == '__main__':
    sample_user_data = {
        'age': 25,
        'email': 'example@example.com',
        'name': 'JohnDoe',
        'password': 'P@ssw0rd'
    }
    
    print(validate_user_data(sample_user_data))