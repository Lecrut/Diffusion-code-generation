def find_users_with_all_groups(user_profiles, required_groups):
    users_with_all_groups = []
    for user in user_profiles:
        user_groups = set(user.get('groups', []))
        if all(group in user_groups for group in required_groups):
            users_with_all_groups.append(user)
    return users_with_all_groups
if __name__ == '__main__':
    user_data = [
        {'id': 1, 'name': 'Alice', 'groups': ['admin', 'dev']},
        {'id': 2, 'name': 'Bob', 'groups': ['dev', 'qa']},
        {'id': 3, 'name': 'Charlie', 'groups': ['admin', 'qa', 'dev']},
        {'id': 4, 'name': 'David', 'groups': ['qa']}
    ]
    required_memberships = [
        ['admin', 'dev'],
        ['qa']
    ]
    result = []
    for req in required_memberships:
        matching_users = []
        for user in user_data:
            user_groups = set(user.get('groups', []))
            if all(group in user_groups for group in req):
                matching_users.append(user)
        result.extend(matching_users)
    print(result)