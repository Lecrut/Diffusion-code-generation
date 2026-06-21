def evaluate_voting_eligibility(age: int, has_criminal_record: bool, is_citizen: bool) -> bool:
    if age < 18:
        return False
    if is_citizen is not True:
        return False
    if has_criminal_record is True:
        return False
    return True

if __name__ == '__main__':
    candidate_age = 20
    candidate_has_record = False
    candidate_is_citizen = True
    result = evaluate_voting_eligibility(candidate_age, candidate_has_record, candidate_is_citizen)
    print(result)