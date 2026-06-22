def is_voting_eligible(age: int, is_citizen: bool) -> bool:
    if age is None or age < 0:
        return False
    if not isinstance(age, int) or isinstance(age, bool):
        return False
    return age >= 18 and is_citizen

if __name__ == '__main__':
    result = is_voting_eligible(20, True)
    print(result)
    result_negative = is_voting_eligible(-5, True)
    print(result_negative)
    result_non_citizen = is_voting_eligible(25, False)
    print(result_non_citizen)
    result_underage = is_voting_eligible(17, True)
    print(result_underage)
    result_boundary = is_voting_eligible(18, True)
    print(result_boundary)