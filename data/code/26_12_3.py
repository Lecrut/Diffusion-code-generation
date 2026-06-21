def is_eligible_to_vote(age, has_criminal_record, is_citizen):
    if not isinstance(age, int) or age < 0:
        return False
    if not isinstance(has_criminal_record, bool):
        return False
    if not isinstance(is_citizen, bool):
        return False
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        (19, False, True),
        (17, False, True),
        (25, True, True),
        (30, False, False),
        (18, False, True),
        (100, False, True)
    ]
    for age, record, citizen in test_cases:
        result = is_eligible_to_vote(age, record, citizen)
        print(f"Age: {age}, Criminal Record: {record}, Citizen: {citizen} -> Eligible: {result}")