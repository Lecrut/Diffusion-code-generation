def is_voting_eligible(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    return age >= 18 and is_citizen

if __name__ == '__main__':
    print(is_voting_eligible(25, True))
    print(is_voting_eligible(17, True))
    print(is_voting_eligible(30, False))
    print(is_voting_eligible(-5, True))