def validate_user_data(user_data):
    criteria = {
        'age': lambda x: x > 0,
        'email': lambda x: '@' in x,
        'name': lambda x: len(x) > 2
    }
    
    for key, value in user_data.items():
        if key in criteria and not criteria[key](value):
            return False
    return True

if __name__ == '__main__':
    sample_user_data = {
        'age': 30,
        'email': 'example@example.com',
        'name': 'John'
    }
    
    print(validate_user_data(sample_user_data))