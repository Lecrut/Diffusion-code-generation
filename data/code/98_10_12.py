def validate_user_access(age, access_level, subscription_status):
    def check_age(val):
        if not isinstance(val, int) or val < 0:
            raise ValueError("Age must be a non-negative integer")
        return val >= 18

    def check_level(val):
        valid_levels = ('admin', 'moderator', 'subscriber')
        if val not in valid_levels:
            raise ValueError(f"Access level must be one of {valid_levels}")
        return val

    def check_subscription(val):
        if val not in ('active', 'expired', 'cancelled'):
            raise ValueError("Subscription status must be active, expired, or cancelled")
        return val

    is_adult = check_age(age)
    level = check_level(access_level)
    status = check_subscription(subscription_status)

    if not is_adult:
        return False

    if level == 'admin':
        return True

    if level == 'moderator' and status == 'active':
        return True

    if level == 'subscriber' and status == 'active':
        return True

    return False

if __name__ == '__main__':
    result = validate_user_access(25, 'moderator', 'active')
    print(result)