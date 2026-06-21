AUTHORIZED_MEMBERS = {'user1': True, 'user2': True, 'user3': True}

def is_user_authorized(user_id):
    return AUTHORIZED_MEMBERS.get(user_id, False)

if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))