VOTING_RULES = {"minimum_age": 18, "allow_negative": False}

def validate_voting_eligibility(age):
    is_number = isinstance(age, (int, float))
    if not is_number:
        raise TypeError("Age must be numeric")
    is_non_negative = age >= 0
    if not is_non_negative:
        raise ValueError("Age must be non-negative")
    meets_minimum = age >= VOTING_RULES["minimum_age"]
    return meets_minimum

if __name__ == '__main__':
    ages_to_check = [20, 17, -5, 18, 65]
    for test_age in ages_to_check:
        try:
            result = validate_voting_eligibility(test_age)
            print(result)
        except (TypeError, ValueError) as e:
            print(False)