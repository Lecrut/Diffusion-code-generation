def is_user_authorized(user_id):
    authorized_members = ['user1', 'user2', 'user3']
    return user_id in authorized_members

if __name__ == '__main__':
    sample_user_id = 'user2'
    print(is_user_authorized(sample_user_id))