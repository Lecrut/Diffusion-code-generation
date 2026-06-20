def validate_user_data(user_id):
    user_data = {
        'user_id': 12345,
        'email': 'example@example.com',
        'age': 28,
        'is_active': True
    }

    def check_id(id):
        return id == user_data['user_id']

    def check_email(email):
        return email == user_data['email']

    def check_age(age):
        return age >= 18

    def check_active(active):
        return active is True

    if not check_id(user_id):
        return False
    if not check_email(user_data['email']):
        return False
    if not check_age(user_data['age']):
        return False
    if not check_active(user_data['is_active']):
        return False

    return True

if __name__ == '__main__':
    print(validate_user_data(12345))