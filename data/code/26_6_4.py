def validate_voting_eligibility(age):
    if age < 0:
        return False
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    print(validate_voting_eligibility(20))
    print(validate_voting_eligibility(17))
    print(validate_voting_eligibility(-5))