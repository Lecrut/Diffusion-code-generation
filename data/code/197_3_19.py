authorized_members = {'user1': True, 'user2': True, 'user3': True}

def is_user_authorized(user_id):
    if not isinstance(user_id, str) or not user_id:
        return False
    return authorized_members.get(user_id, False)

if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))