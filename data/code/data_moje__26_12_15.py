def evaluate_voting_eligibility(age, is_citizen, has_criminal_record):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    sample_age = 25
    sample_is_citizen = True
    sample_has_criminal_record = False
    result = evaluate_voting_eligibility(sample_age, sample_is_citizen, sample_has_criminal_record)
    print(result)