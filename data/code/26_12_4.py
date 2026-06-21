def check_voting_eligibility(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    result1 = check_voting_eligibility(25, False, True)
    result2 = check_voting_eligibility(16, False, True)
    result3 = check_voting_eligibility(30, True, True)
    result4 = check_voting_eligibility(20, False, False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)