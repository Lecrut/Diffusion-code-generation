def get_access(age, has_permission):
    if not isinstance(age, int) or not isinstance(has_permission, bool):
        raise ValueError("age must be an integer and has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 or has_permission

if __name__ == '__main__':
    result = get_access(16, True)
    print(result)