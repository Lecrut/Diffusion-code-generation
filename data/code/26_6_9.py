def validate_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        return False
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    print(validate_voting_eligibility(19))
    print(validate_voting_eligibility(15))
    print(validate_voting_eligibility(-1))
    print(validate_voting_eligibility(18))