def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18 and is_citizen

if __name__ == '__main__':
    print(is_eligible_to_vote(20, True))
    print(is_eligible_to_vote(16, True))
    print(is_eligible_to_vote(20, False))
    print(is_eligible_to_vote(18, True))
    print(is_eligible_to_vote(0, True))