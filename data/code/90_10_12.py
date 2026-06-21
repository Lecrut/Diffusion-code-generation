def validate_age(value):
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError("age must be an integer")
    if value < 0:
        raise ValueError("age cannot be negative")
    return value

def validate_permission(value):
    if not isinstance(value, bool):
        raise ValueError("permission must be a boolean")
    return value

def grant_access(age, has_permission):
    valid_age = validate_age(age)
    valid_permission = validate_permission(has_permission)
    return valid_age >= 18 or valid_permission

if __name__ == '__main__':
    result = grant_access(17, True)
    print(result)