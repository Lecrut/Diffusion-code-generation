def evaluate_voting_eligibility(age, has_criminal_record, is_citizen):
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    result1 = evaluate_voting_eligibility(25, False, True)
    print(result1)
    result2 = evaluate_voting_eligibility(16, False, True)
    print(result2)
    result3 = evaluate_voting_eligibility(30, True, True)
    print(result3)
    result4 = evaluate_voting_eligibility(20, False, False)
    print(result4)
    result5 = evaluate_voting_eligibility(18, False, True)
    print(result5)