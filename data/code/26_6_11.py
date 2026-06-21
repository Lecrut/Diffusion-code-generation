def validate_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return False
    if age < 0:
        return False
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    print(validate_voting_eligibility(17))
    print(validate_voting_eligibility(18))
    print(validate_voting_eligibility(25))
    print(validate_voting_eligibility(-5))
    print(validate_voting_eligibility(0))