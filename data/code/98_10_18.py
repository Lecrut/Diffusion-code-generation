MINIMUM_AGE = 18
REQUIRED_ACCESS_LEVELS = ('admin', 'premium_user', 'vip')
REQUIRED_SUBSCRIPTION = 'active'

def verify_access_credentials(age, access_level, subscription_status):
    if age < MINIMUM_AGE:
        return False
    if access_level not in REQUIRED_ACCESS_LEVELS:
        raise ValueError("Invalid access level")
    if subscription_status != REQUIRED_SUBSCRIPTION:
        return False
    return True

if __name__ == '__main__':
    user_age = 25
    user_level = 'premium_user'
    user_sub = 'active'
    outcome = verify_access_credentials(user_age, user_level, user_sub)
    print(outcome)