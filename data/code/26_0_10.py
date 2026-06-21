MINIMUM_VOTING_AGE = 18

def verify_age_validity(age_value):
    if not isinstance(age_value, (int, float)):
        raise TypeError("Age must be numeric")
    if age_value < 0:
        raise ValueError("Age must be non-negative")
    return True

def check_voting_eligibility(age):
    verify_age_validity(age)
    return age >= MINIMUM_VOTING_AGE

if __name__ == '__main__':
    test_cases = [16, 17, 18, 19, 65]
    for age_input in test_cases:
        eligibility_status = check_voting_eligibility(age_input)
        print(eligibility_status)