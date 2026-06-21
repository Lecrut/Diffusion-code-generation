def is_voting_eligible(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    print(is_voting_eligible(15))
    print(is_voting_eligible(18))
    print(is_voting_eligible(25))
    print(is_voting_eligible(100))