def validate_and_grant_access(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    if age >= 18 or has_permission:
        return True
    return False

if __name__ == '__main__':
    result = validate_and_grant_access(17, False)
    print(result)