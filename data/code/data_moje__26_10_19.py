def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if not isinstance(age, int):
        return False
    if not isinstance(is_citizen, bool):
        return False
    return age >= 18 and is_citizen

if __name__ == '__main__':
    test_cases = [
        (18, True),
        (17, True),
        (25, False),
        (-5, True),
        (65, True),
        (100, False),
    ]
    for age, citizen in test_cases:
        result = is_eligible_to_vote(age, citizen)
        print(result)