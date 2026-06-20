def validate_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Invalid age")
    return True

def validate_access_level(level):
    if level not in ['admin', 'user']:
        raise ValueError("Invalid access level")
    return True

def validate_subscription_status(status):
    if status != 'active':
        raise ValueError("Invalid subscription status")
    return True

if __name__ == '__main__':
    age = 25
    access_level = 'admin'
    subscription_status = 'active'

    try:
        if validate_age(age) and validate_access_level(access_level) and validate_subscription_status(subscription_status):
            print("Access granted")
        else:
            print("Access denied")
    except ValueError as e:
        print(e)