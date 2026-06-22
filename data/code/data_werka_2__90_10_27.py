def check_access(age, has_permission):
    if not isinstance(age, int) or not isinstance(has_permission, bool):
        raise ValueError("Invalid input types")
    if age < 0 or age > 150:
        raise ValueError("Age out of range")
    return age >= 18 or has_permission

if __name__ == '__main__':
    result = check_access(16, True)
    print(result)