def is_user_authorized(user_id):
    authorized_members = ['user123', 'user456', 'user789']
    return user_id in authorized_members

if __name__ == '__main__':
    sample_user_id = 'user456'
    print(is_user_authorized(sample_user_id))