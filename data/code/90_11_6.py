def validate_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer")
    return True

def validate_permission(permission):
    if permission not in ['yes', 'no']:
        raise ValueError("Permission must be 'yes' or 'no'")
    return True

def check_access(age, permission):
    try:
        validate_age(age)
        validate_permission(permission)
        return age >= 18 or permission == 'yes'
    except ValueError as e:
        print(e)
        return False

if __name__ == '__main__':
    print(check_access(20, 'no'))
    print(check_access(15, 'yes'))