def check_permissions(user_role, is_admin, has_access_code):
    return (user_role == 'admin' or is_admin) and has_access_code

if __name__ == '__main__':
    print(check_permissions('admin', False, True))
    print(check_permissions('user', True, False))
    print(check_permissions('user', False, True))