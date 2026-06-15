def find_users_with_groups(user_profiles, required_groups):
    user_group_map = {}
    for user in user_profiles:
        user_id = user['id']
        user_group_map[user_id] = set(user.get('groups', []))
    satisfying_users = []
    for req_group in required_groups:
        current_satisfying_users = []
        for user_id, user_groups in user_group_map.items():
            if req_group in user_groups:
                current_satisfying_users.append(user_id)
        if not current_satisfying_users:
            return []
    final_satisfying_users = set()
    for req_group in required_groups:
        satisfied_by_this_group = set()
        for user_id, user_groups in user_group_map.items():
            if req_group in user_groups:
                satisfied_by_this_group.add(user_id)
        if not satisfied_by_this_group:
            return []
        final_satisfying_users.intersection_update(satisfied_by_this_group)
    result = [user_profiles[user['id']] for user in user_profiles if user['id'] in final_satisfying_users]
    return result
if __name__ == '__main__':
    user_data = [
        {'id': 1, 'name': 'Alice', 'groups': ['admin', 'dev']},
        {'id': 2, 'name': 'Bob', 'groups': ['dev', 'qa']},
        {'id': 3, 'name': 'Charlie', 'groups': ['admin']},
        {'id': 4, 'name': 'David', 'groups': ['qa', 'dev']}
    ]
    required_groups_1 = ['admin']
    result_1 = find_users_with_groups(user_data, required_groups_1)
    print("Result 1:", result_1)
    required_groups_2 = ['dev', 'qa']
    result_2 = find_users_with_groups(user_data, required_groups_2)
    print("Result 2:", result_2)
    required_groups_3 = ['admin', 'qa']
    result_3 = find_users_with_groups(user_data, required_groups_3)
    print("Result 3:", result_3)
    required_groups_4 = ['unknown_group']
    result_4 = find_users_with_groups(user_data, required_groups_4)
    print("Result 4:", result_4)