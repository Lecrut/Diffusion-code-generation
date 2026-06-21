def is_user_authorized(user_id):
    authorized_members = {'user1': True, 'user2': True, 'user3': True}
    return authorized_members.get(user_id, False)

if __name__ == '__main__':
    print(is_user_authorized('user2'))
    print(is_user_authorized('user4'))