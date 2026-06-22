def check_access(age, access_level, subscription_status):
    if age < 18:
        return False
    if access_level not in ('admin', 'user', 'guest'):
        raise ValueError(f"Unsupported access level: {access_level}")
    if subscription_status not in ('active', 'expired', 'cancelled'):
        raise ValueError(f"Unsupported subscription status: {subscription_status}")
    
    if age >= 18 and access_level == 'admin' and subscription_status == 'active':
        return True
    return False

if __name__ == '__main__':
    result = check_access(25, 'admin', 'active')
    print(result)