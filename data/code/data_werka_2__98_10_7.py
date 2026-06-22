def check_access(age, access_level, subscription_status):
    if age < 18:
        return False
    if access_level not in ('admin', 'user', 'guest'):
        raise ValueError("Invalid access level")
    if subscription_status not in ('active', 'inactive'):
        raise ValueError("Invalid subscription status")
    if access_level == 'admin':
        return True
    if access_level == 'user' and subscription_status == 'active':
        return True
    if access_level == 'guest' and age >= 21:
        return True
    return False

if __name__ == '__main__':
    result = check_access(25, 'user', 'active')
    print(result)