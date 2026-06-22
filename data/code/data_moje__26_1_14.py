def check_voting_eligibility(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18

if __name__ == '__main__':
    print(check_voting_eligibility(21))
    print(check_voting_eligibility(17))
    print(check_voting_eligibility(18))
    print(check_voting_eligibility(100))
    print(check_voting_eligibility(-5))