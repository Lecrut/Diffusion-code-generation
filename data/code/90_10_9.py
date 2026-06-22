ACCESS_RULES = {
    "minor_no_perm": 15,
    "minor_with_perm": 16,
    "adult_no_perm": 19,
    "adult_with_perm": 20
}

def grant_access(age, has_permission):
    if not isinstance(age, int) or not isinstance(has_permission, bool):
        raise ValueError("age must be an integer and has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    condition_key = f"{'minor' if age < 18 else 'adult'}_{'no_perm' if not has_permission else 'with_perm'}"
    return condition_key in ACCESS_RULES

if __name__ == '__main__':
    test_cases = [
        (15, False),
        (16, True),
        (19, False),
        (20, True)
    ]
    for age, perm in test_cases:
        result = grant_access(age, perm)
        print(result)