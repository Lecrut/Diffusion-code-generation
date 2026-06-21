def check_access(age, has_permission):
    if not isinstance(age, int) or not isinstance(has_permission, bool):
        raise ValueError("Invalid input types")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18 or has_permission

if __name__ == '__main__':
    result = check_access(16, True)
    print(result)