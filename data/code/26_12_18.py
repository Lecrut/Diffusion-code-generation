def evaluate_voting_eligibility(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    result1 = evaluate_voting_eligibility(20, False, True)
    result2 = evaluate_voting_eligibility(17, False, True)
    result3 = evaluate_voting_eligibility(25, True, True)
    result4 = evaluate_voting_eligibility(30, False, False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)