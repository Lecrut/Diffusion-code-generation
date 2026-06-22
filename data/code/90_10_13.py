def get_access_level(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    rules = {
        "child_no_perm": (False, False),
        "child_with_perm": (False, True),
        "teen_no_perm": (True, False),
        "teen_with_perm": (True, True),
        "adult_no_perm": (True, False),
        "adult_with_perm": (True, True)
    }
    category = "child" if age < 13 else "teen" if age < 18 else "adult"
    perm_str = "with_perm" if has_permission else "no_perm"
    key = f"{category}_{perm_str}"
    is_adult = age >= 18
    return is_adult or has_permission

if __name__ == '__main__':
    result = get_access_level(15, True)
    print(result)