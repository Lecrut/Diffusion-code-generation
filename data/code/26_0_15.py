VOTING_THRESHOLD = 18

def _validate_age_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Age must be a numeric type")
    if value < 0:
        raise ValueError("Age cannot be negative")
    return int(value)

def is_eligible_to_vote(age):
    validated_age = _validate_age_input(age)
    return validated_age >= VOTING_THRESHOLD

if __name__ == '__main__':
    test_cases = [17, 18, 25, 65, 10]
    for age in test_cases:
        print(is_eligible_to_vote(age))