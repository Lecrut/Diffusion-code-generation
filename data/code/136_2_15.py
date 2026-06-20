def validate_user_data(user_data):
    required_keys = ['name', 'age', 'email']
    if not all(key in user_data for key in required_keys):
        return False

    if user_data['age'] < 18:
        return False

    if '@' not in user_data['email']:
        return False

    return True

if __name__ == '__main__':
    sample_user_data = {
        'name': 'John Doe',
        'age': 25,
        'email': 'john.doe@example.com'
    }
    print(validate_user_data(sample_user_data))