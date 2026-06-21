user_map = {}

def map_users(user_ids):
    return {user_id: idx for idx, user_id in enumerate(user_ids)}

if __name__ == '__main__':
    sample_user_ids = ["alice", "bob", "charlie", "david"]
    mapped_indices = map_users(sample_user_ids)
    print(mapped_indices)