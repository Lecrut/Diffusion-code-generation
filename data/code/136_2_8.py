def validate_user_data(user_id):
    user_data = {'user1': {'age': 25, 'email': 'user1@example.com'}, 'user2': {'age': 30, 'email': 'user2@example.com'}, 'user3': {'age': 35, 'email': 'user3@example.com'}}
    if user_id not in user_data:
        return False
    user_info = user_data[user_id]
    if user_info['age'] < 18:
        return False
    if '@' not in user_info['email']:
        return False
    return True
if __name__ == '__main__':
    print(validate_user_data('user1'))
    print(validate_user_data('user4'))