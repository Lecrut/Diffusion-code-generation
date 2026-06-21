def is_user_authorized(user_id):
    authorized_users = ['user1', 'user2', 'user3']
    return user_id in authorized_users
if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))