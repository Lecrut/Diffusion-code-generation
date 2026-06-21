def is_user_authorized(user_id):
    authorized_members = ['user1', 'user2', 'user3']
    if not isinstance(user_id, str) or not user_id:
        return False
    return user_id in authorized_members
if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))
    print(is_user_authorized(''))
    print(is_user_authorized(123))