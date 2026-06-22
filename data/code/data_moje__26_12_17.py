def is_voting_eligible(age, has_criminal_record, is_citizen):
    if not isinstance(age, int) or age < 0:
        return False
    if not isinstance(is_citizen, bool) or not is_citizen:
        return False
    if age < 18:
        return False
    if isinstance(has_criminal_record, bool) and has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    sample_age = 25
    sample_criminal_record = False
    sample_citizen = True
    result = is_voting_eligible(sample_age, sample_criminal_record, sample_citizen)
    print(result)