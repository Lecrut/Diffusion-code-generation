def is_user_authorized(user_id):
    authorized_members = {'user1': True, 'user2': True, 'user3': True}
    if user_id not in authorized_members:
        raise ValueError("Invalid user ID")
    return authorized_members[user_id]

if __name__ == '__main__':
    try:
        print(is_user_authorized('user2'))
        print(is_user_authorized('user4'))
    except ValueError as e:
        print(e)