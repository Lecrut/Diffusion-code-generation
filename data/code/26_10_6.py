def determine_voting_eligibility(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if age < 18:
        return False
    return is_citizen

if __name__ == '__main__':
    print(determine_voting_eligibility(20, True))
    print(determine_voting_eligibility(15, True))
    print(determine_voting_eligibility(20, False))
    print(determine_voting_eligibility(-5, True))
    print(determine_voting_eligibility(18, True))
    print(determine_voting_eligibility(17, True))