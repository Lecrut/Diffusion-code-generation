def evaluate_entry(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 or has_permission

if __name__ == '__main__':
    result = evaluate_entry(17, False)
    print(result)