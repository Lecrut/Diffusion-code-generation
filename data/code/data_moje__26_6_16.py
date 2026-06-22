def is_eligible_to_vote(age):
    if age < 0:
        raise ValueError("Age must be non-negative")
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    print(is_eligible_to_vote(17))
    print(is_eligible_to_vote(18))
    print(is_eligible_to_vote(25))