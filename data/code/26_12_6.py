def evaluate_voting_eligibility(age, has_criminal_record, is_citizen):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if not isinstance(has_criminal_record, bool):
        raise TypeError("has_criminal_record must be a boolean")
    if not isinstance(is_citizen, bool):
        raise TypeError("is_citizen must be a boolean")
    
    if not is_citizen:
        return False
    if age < 18:
        return False
    if has_criminal_record:
        return False
    return True

if __name__ == '__main__':
    print(evaluate_voting_eligibility(25, False, True))
    print(evaluate_voting_eligibility(16, False, True))
    print(evaluate_voting_eligibility(25, True, True))
    print(evaluate_voting_eligibility(25, False, False))