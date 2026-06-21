def map_user_ids_to_indices(user_ids):
    return {user_id: index for index, user_id in enumerate(user_ids)}

if __name__ == '__main__':
    sample_user_ids = ['user1', 'user2', 'user3']
    mapped_indices = map_user_ids_to_indices(sample_user_ids)
    print(mapped_indices)