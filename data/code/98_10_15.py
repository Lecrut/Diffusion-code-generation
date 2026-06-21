def check_access(age, access_level, subscription_status):
    if age < 18:
        return False
    if access_level not in ('admin', 'user', 'guest'):
        raise ValueError("Invalid access level")
    if subscription_status not in ('active', 'inactive', 'expired'):
        raise ValueError("Invalid subscription status")
    
    if age >= 21 and access_level == 'admin' and subscription_status == 'active':
        return True
    if age >= 18 and access_level == 'user' and subscription_status == 'active':
        return True
    if age >= 18 and access_level == 'guest' and subscription_status == 'inactive':
        return True
    return False

if __name__ == '__main__':
    result = check_access(25, 'admin', 'active')
    print(result)