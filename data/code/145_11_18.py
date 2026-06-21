def check_access(user_role, resource_type, action):
    is_admin = user_role == 'admin'
    can_read = resource_type in ['public', 'user'] or is_admin
    can_write = resource_type == 'user' or is_admin
    can_execute = resource_type == 'script' and (is_admin or action == 'view')
    
    return can_read and can_write and can_execute

if __name__ == '__main__':
    print(check_access('admin', 'public', 'view'))
    print(check_access('user', 'user', 'edit'))
    print(check_access('guest', 'script', 'run'))