MINIMUM_AGE = 18
REQUIRED_PERMISSION = True

def can_grant_access(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= MINIMUM_AGE or has_permission

if __name__ == '__main__':
    sample_age = 17
    sample_permission = False
    outcome = can_grant_access(sample_age, sample_permission)
    print(outcome)