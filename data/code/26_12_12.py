def is_eligible_to_vote(age, has_criminal_record, is_citizen):
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
        (22, False, False),
        (45, True, False)
    ]
    for age, record, citizenship in sample_cases:
        result = is_eligible_to_vote(age, record, citizenship)
        print(f"Age: {age}, Criminal Record: {record}, Citizen: {citizenship} -> Eligible: {result}")