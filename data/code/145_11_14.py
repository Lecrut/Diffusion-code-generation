def check_permissions(user_role, resource_type, action):
    if not isinstance(user_role, str) or not isinstance(resource_type, str) or (not isinstance(action, str)):
        raise ValueError('Invalid input types. Expected strings for user_role, resource_type, and action.')
    permissions = {'admin': {'file': ['read', 'write'], 'database': ['read', 'write']}, 'user': {'file': ['read'], 'database': ['read']}}
    if user_role not in permissions:
        return False
    if resource_type not in permissions[user_role]:
        return False
    return action in permissions[user_role][resource_type]
if __name__ == '__main__':
    print(check_permissions('admin', 'file', 'read'))
    print(check_permissions('user', 'database', 'write'))