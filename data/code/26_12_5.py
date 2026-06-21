def is_eligible_to_vote(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        (25, False, True),
        (17, False, True),
        (30, True, True),
        (40, False, False),
        (21, False, True)
    ]

    for age, criminal, citizen in test_cases:
        result = is_eligible_to_vote(age, criminal, citizen)
        print(f"Age: {age}, Criminal: {criminal}, Citizen: {citizen} -> Eligible: {result}")