def validate_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    print(validate_voting_eligibility(20))
    print(validate_voting_eligibility(17))
    print(validate_voting_eligibility(-5))
    print(validate_voting_eligibility(18))
    print(validate_voting_eligibility(65))