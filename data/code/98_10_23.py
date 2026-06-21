MINIMUM_AGE = 18
REQUIRED_ACCESS_LEVELS = ('admin', 'premium', 'vip')
REQUIRED_SUBSCRIPTION = 'active'

def verify_access_criteria(age, access_level, subscription_status):
    if age < MINIMUM_AGE:
        return False
    if access_level not in REQUIRED_ACCESS_LEVELS:
        raise ValueError("Invalid access level")
    if subscription_status != REQUIRED_SUBSCRIPTION:
        return False
    return True

if __name__ == '__main__':
    sample_age = 25
    sample_level = 'premium'
    sample_sub = 'active'
    outcome = verify_access_criteria(sample_age, sample_level, sample_sub)
    print(outcome)