def find_users_with_groups(user_profiles, required_groups):
    user_group_map = {}
    for user in user_profiles:
        user_id = user['id']
        user_group_map[user_id] = set(user.get('groups', []))
    matching_users = []
    for required_group in required_groups:
        current_matches = set()
        for user_id, groups in user_group_map.items():
            if required_group in groups:
                current_matches.add(user_id)
        if not current_matches:
            return []
    final_matching_users = []
    for required_group in required_groups:
        potential_users = set()
        for user_id, groups in user_group_map.items():
            if required_group in groups:
                potential_users.add(user_id)
        if not potential_users:
            return []
        if len(required_groups) == 1:
            final_matching_users = list(potential_users)
            break
        else:
            pass
    if not required_groups:
        return []
    all_user_ids = set(user_group_map.keys())
    intersection_of_all_users = all_user_ids
    for required_group in required_groups:
        current_group_users = set()
        for user_id, groups in user_group_map.items():
            if required_group in groups:
                current_group_users.add(user_id)
        intersection_of_all_users.intersection_update(current_group_users)
    return list(intersection_of_all_users)
if __name__ == '__main__':
    user_profiles = [
        {'id': 1, 'name': 'Alice', 'groups': ['admin', 'dev']},
        {'id': 2, 'name': 'Bob', 'groups': ['user', 'dev']},
        {'id': 3, 'name': 'Charlie', 'groups': ['user', 'qa']},
        {'id': 4, 'name': 'David', 'groups': ['admin', 'qa']}
    ]
    required_groups1 = ['admin']
    result1 = find_users_with_groups(user_profiles, required_groups1)
    print(f"Required: {required_groups1}")
    print(f"Result: {result1}\n")
    required_groups2 = ['dev', 'qa']
    result2 = find_users_with_groups(user_profiles, required_groups2)
    print(f"Required: {required_groups2}")
    print(f"Result: {result2}\n")
    required_groups3 = ['admin', 'user']
    result3 = find_users_with_groups(user_profiles, required_groups3)
    print(f"Required: {required_groups3}")
    print(f"Result: {result3}\n")
    required_groups4 = ['dev', 'qa', 'nonexistent']
    result4 = find_users_with_groups(user_profiles, required_groups4)
    print(f"Required: {required_groups4}")
    print(f"Result: {result4}\n")
    required_groups5 = []
    result5 = find_users_with_groups(user_profiles, required_groups5)
    print(f"Required: {required_groups5}")
    print(f"Result: {result5}\n")