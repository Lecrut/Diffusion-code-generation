def is_user_authorized(user_id):
    authorized_members = ['admin', 'moderator', 'viewer']
    return user_id in authorized_members

if __name__ == '__main__':
    sample_users = ['user123', 'moderator', 'guest']
    for user in sample_users:
        print(f'User {user} is authorized: {is_user_authorized(user)}')