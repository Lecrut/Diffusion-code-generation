def map_user_ids_to_indices(user_ids):
    if not all(isinstance(uid, str) and uid.isalnum() for uid in user_ids):
        raise ValueError("All user IDs must be alphanumeric strings.")
    
    return {uid: idx for idx, uid in enumerate(user_ids)}

if __name__ == '__main__':
    sample_user_ids = ["user1", "user2", "user3"]
    try:
        result = map_user_ids_to_indices(sample_user_ids)
        print(result)
    except ValueError as e:
        print(e)