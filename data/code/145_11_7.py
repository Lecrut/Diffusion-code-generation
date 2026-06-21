def check_access(user_role, resource_type, action):
    is_admin = user_role == 'admin'
    can_read = resource_type in ('public', 'user') or is_admin
    can_write = resource_type == 'user' and (action == 'edit' or is_admin)
    return can_read and can_write
if __name__ == '__main__':
    print(check_access('admin', 'user', 'edit'))
    print(check_access('user', 'public', 'view'))
    print(check_access('guest', 'private', 'delete'))