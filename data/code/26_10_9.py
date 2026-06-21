def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    return age >= 18 and is_citizen

if __name__ == '__main__':
    print(is_eligible_to_vote(20, True))
    print(is_eligible_to_vote(15, True))
    print(is_eligible_to_vote(20, False))
    print(is_eligible_to_vote(-5, True))
    print(is_eligible_to_vote(18, True))
    print(is_eligible_to_vote(17, True))