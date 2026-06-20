def validate_user_data(user_id):
    user_data = {
        'user_id': 123,
        'email': 'example@example.com',
        'age': 25,
        'is_active': True
    }
    
    if user_id != user_data['user_id']:
        return False
    
    if not '@' in user_data['email']:
        return False
    
    if user_data['age'] < 18:
        return False
    
    if not user_data['is_active']:
        return False
    
    return True

if __name__ == '__main__':
    print(validate_user_data(123))