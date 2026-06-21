def is_user_authorized(user_id):
    authorized_ids = ['user123', 'user456', 'user789']
    return user_id in authorized_ids
if __name__ == '__main__':
    print(is_user_authorized('user456'))
    print(is_user_authorized('user000'))