USER_IDS = {
    "user1": 0,
    "user2": 1,
    "user3": 2,
}

def map_user_ids(user_identifiers):
    return {user_id: index for index, user_id in enumerate(user_identifiers)}

if __name__ == '__main__':
    sample_users = ["user1", "user2", "user3"]
    mapped_users = map_user_ids(sample_users)
    print(mapped_users)