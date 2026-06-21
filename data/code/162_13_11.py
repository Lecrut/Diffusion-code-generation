def map_user_ids(user_ids):
    return {user_id: idx for idx, user_id in enumerate(user_ids)}

if __name__ == '__main__':
    sample_user_ids = ['user1', 'user2', 'user3']
    print(map_user_ids(sample_user_ids))