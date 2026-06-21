def _validate_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

def is_eligible_to_vote(age):
    _validate_age(age)
    return age >= 18

if __name__ == '__main__':
    test_cases = [15, 18, 25, 0, -1]
    for case in test_cases:
        try:
            result = is_eligible_to_vote(case)
            print(result)
        except Exception as e:
            print(repr(e))