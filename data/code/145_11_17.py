def check_access(user_role, is_admin, has_permission):
    return (user_role == 'admin' or is_admin) and has_permission

if __name__ == '__main__':
    print(check_access('admin', False, True))
    print(check_access('user', True, False))
    print(check_access('guest', False, False))