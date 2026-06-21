def check_voting_eligibility(age, has_criminal_record, is_citizen):
    if age < 18:
        return False
    if not is_citizen:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    result = check_voting_eligibility(20, False, True)
    print(result)