def is_user_authorized(user_id):
    authorized_members = ['admin', 'manager', 'developer']
    return user_id in authorized_members

if __name__ == '__main__':
    sample_user_ids = ['admin', 'user', 'manager']
    for uid in sample_user_ids:
        print(f"User ID '{uid}' is authorized: {is_user_authorized(uid)}")