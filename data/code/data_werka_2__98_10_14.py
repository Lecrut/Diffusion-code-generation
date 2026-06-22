def verify_access(age, access_level, subscription_status):
    valid_levels = ('admin', 'premium', 'standard')
    valid_statuses = ('active', 'expired', 'cancelled')
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    if access_level not in valid_levels:
        raise ValueError("Invalid access level")
    if subscription_status not in valid_statuses:
        raise ValueError("Invalid subscription status")
    
    is_minor = age < 18
    is_admin = access_level == 'admin'
    is_premium = access_level == 'premium'
    is_active = subscription_status == 'active'
    
    if is_admin:
        return True
    
    if is_premium and is_active:
        return True
    
    if not is_minor and is_active:
        return True
        
    return False

if __name__ == '__main__':
    user_age = 30
    user_level = 'premium'
    user_sub = 'active'
    
    access_granted = verify_access(user_age, user_level, user_sub)
    print(access_granted)