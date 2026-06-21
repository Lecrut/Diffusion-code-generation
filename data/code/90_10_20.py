def evaluate_access(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 or has_permission

if __name__ == '__main__':
    age_val = 17
    perm_val = False
    result = evaluate_access(age_val, perm_val)
    print(result)