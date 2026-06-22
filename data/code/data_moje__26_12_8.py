def check_voting_eligibility(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    sample_age = 25
    sample_criminal_record = False
    sample_citizen = True
    result = check_voting_eligibility(sample_age, sample_criminal_record, sample_citizen)
    print(result)