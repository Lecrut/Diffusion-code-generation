def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

def validate_permission(has_permission):
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    return has_permission

def check_access(age, has_permission):
    valid_age = validate_age(age)
    valid_perm = validate_permission(has_permission)
    return valid_age >= 18 or valid_perm

if __name__ == '__main__':
    result = check_access(16, True)
    print(result)