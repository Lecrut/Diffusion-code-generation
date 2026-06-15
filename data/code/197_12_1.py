def find_users_with_all_groups(user_profiles, required_groups):
    satisfied_users = []
    for user in user_profiles:
        user_groups = set(user.get('groups', []))
        if all(group in user_groups for group in required_groups):
            satisfied_users.append(user)
    return satisfied_users
if __name__ == '__main__':
    user_data = [
        {'id': 1, 'name': 'Alice', 'groups': ['admin', 'dev']},
        {'id': 2, 'name': 'Bob', 'groups': ['user', 'dev']},
        {'id': 3, 'name': 'Charlie', 'groups': ['admin', 'user', 'qa']},
        {'id': 4, 'name': 'David', 'groups': ['user']},
        {'id': 5, 'name': 'Eve', 'groups': ['dev', 'qa']}
    ]
    required_membership_1 = ['admin', 'user']
    result_1 = find_users_with_all_groups(user_data, required_membership_1)
    print("Result 1:")
    print(result_1)
    required_membership_2 = ['dev', 'qa']
    result_2 = find_users_with_all_groups(user_data, required_membership_2)
    print("\nResult 2:")
    print(result_2)
    required_membership_3 = ['admin', 'dev', 'qa']
    result_3 = find_users_with_all_groups(user_data, required_membership_3)
    print("\nResult 3:")
    print(result_3)