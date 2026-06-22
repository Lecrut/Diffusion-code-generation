def verify_access_credentials(age, access_level, subscription_status):
    min_adult_age = 18
    min_guest_age = 21
    valid_levels = ('admin', 'user', 'guest')
    
    if age < min_adult_age:
        return False
    if access_level not in valid_levels:
        raise ValueError("Access level must be admin, user, or guest")
    if subscription_status not in ('active', 'inactive'):
        raise ValueError("Subscription status must be active or inactive")
        
    is_admin = access_level == 'admin'
    is_user = access_level == 'user'
    is_guest = access_level == 'guest'
    is_subscribed = subscription_status == 'active'
    
    if is_admin:
        return True
    if is_user and is_subscribed:
        return True
    if is_guest and age >= min_guest_age:
        return True
        
    return False

if __name__ == '__main__':
    sample_age = 22
    sample_level = 'guest'
    sample_sub = 'active'
    access_granted = verify_access_credentials(sample_age, sample_level, sample_sub)
    print(access_granted)