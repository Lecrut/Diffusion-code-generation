def evaluate_access(age, access_level, subscription_status):
    is_adult = age >= 18
    is_valid_level = access_level in ('admin', 'user', 'guest')
    is_active_sub = subscription_status == 'active'
    
    if not is_adult:
        return False
    if not is_valid_level:
        raise ValueError("Unsupported access level")
    if not is_active_sub:
        return False
        
    if access_level == 'admin':
        return True
    if access_level == 'user':
        return True
    if access_level == 'guest' and age >= 21:
        return True
    return False

if __name__ == '__main__':
    sample_age = 22
    sample_level = 'guest'
    sample_sub = 'active'
    outcome = evaluate_access(sample_age, sample_level, sample_sub)
    print(outcome)