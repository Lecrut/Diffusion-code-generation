def evaluate_voting_eligibility(age, has_criminal_record, is_citizen):
    if age < 18:
        return False
    if has_criminal_record:
        return False
    if not is_citizen:
        return False
    return True

if __name__ == '__main__':
    eligible = evaluate_voting_eligibility(25, False, True)
    print(eligible)