def can_access(user_age, access_level, subscription_status):
    if user_age >= 18 and access_level == 'admin' and subscription_status:
        return True
    else:
        return False

if __name__ == '__main__':
    print(can_access(25, 'admin', True))
    print(can_access(17, 'user', True))
    print(can_access(25, 'guest', True))
    print(can_access(25, 'admin', False))