authorized_members = {'user123', 'user456', 'user789'}

def is_user_authorized(user_id):
    return user_id in authorized_members
if __name__ == '__main__':
    print(is_user_authorized('user456'))
    print(is_user_authorized('user000'))