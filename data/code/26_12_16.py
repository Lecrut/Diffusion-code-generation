def evaluate_voting_eligibility(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    sample_cases = [
        (25, False, True),
        (17, False, True),
        (30, True, True),
        (45, False, False),
        (19, False, True)
    ]
    for age, record, citizen in sample_cases:
        result = evaluate_voting_eligibility(age, record, citizen)
        print(result)