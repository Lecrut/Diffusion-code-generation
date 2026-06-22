def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if not is_citizen:
        return False
    return age >= 18

if __name__ == '__main__':
    print(is_eligible_to_vote(17, True))
    print(is_eligible_to_vote(18, True))
    print(is_eligible_to_vote(25, False))
    print(is_eligible_to_vote(-5, True))