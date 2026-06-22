def check_entry_eligibility(age, has_permission):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValueError("age must be an integer")
    if not isinstance(has_permission, bool):
        raise ValueError("has_permission must be a boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    meets_age_requirement = age >= 18
    meets_permission_requirement = has_permission
    return meets_age_requirement or meets_permission_requirement

if __name__ == '__main__':
    sample_age = 17
    sample_permission = False
    eligibility = check_entry_eligibility(sample_age, sample_permission)
    print(eligibility)