def check_voting_eligibility(age, has_criminal_record, is_citizen):
    if not isinstance(age, int) or age < 0:
        return False
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    sample1 = check_voting_eligibility(20, False, True)
    sample2 = check_voting_eligibility(17, False, True)
    sample3 = check_voting_eligibility(25, True, True)
    sample4 = check_voting_eligibility(30, False, False)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)