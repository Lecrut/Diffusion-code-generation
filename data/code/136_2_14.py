def validate_user_data(user_info):
    results = {}
    if 'age' in user_info and user_info['age'] >= 18:
        results['is_adult'] = True
    else:
        results['is_adult'] = False
    if 'email' in user_info and '@' in user_info['email']:
        results['valid_email'] = True
    else:
        results['valid_email'] = False
    if 'username' in user_info and len(user_info['username']) >= 4:
        results['valid_username'] = True
    else:
        results['valid_username'] = False
    return results
if __name__ == '__main__':
    sample_user_data = {'age': 25, 'email': 'example@example.com', 'username': 'user123'}
    validation_results = validate_user_data(sample_user_data)
    print(validation_results)