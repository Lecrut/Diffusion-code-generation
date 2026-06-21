def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if not is_citizen:
        return False
    return age >= 18

if __name__ == '__main__':
    test_cases = [
        (18, True),
        (17, True),
        (25, False),
        (-5, True),
        (60, True),
        (0, True),
    ]
    for age, citizen in test_cases:
        result = is_eligible_to_vote(age, citizen)
        print(f"Age: {age}, Citizen: {citizen} -> Eligible: {result}")