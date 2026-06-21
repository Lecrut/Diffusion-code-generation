def is_voting_eligible(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if age < 18:
        return False
    if not is_citizen:
        return False
    return True

if __name__ == '__main__':
    print(is_voting_eligible(20, True))
    print(is_voting_eligible(17, True))
    print(is_voting_eligible(20, False))
    print(is_voting_eligible(-5, True))