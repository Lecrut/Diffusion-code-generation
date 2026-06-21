def map_user_ids(user_ids):
    return {user_id: idx for idx, user_id in enumerate(user_ids)}

if __name__ == '__main__':
    sample_users = ["alice", "bob", "charlie", "dave"]
    mapping = map_user_ids(sample_users)
    print(mapping)