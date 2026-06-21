authorized_users = {'user1': True, 'user2': True, 'user3': True}

def is_user_authorized(user_id):
    return authorized_users.get(user_id, False)

if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))