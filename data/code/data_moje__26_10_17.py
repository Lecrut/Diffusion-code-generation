def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        return False
    if not isinstance(age, int):
        return False
    if not isinstance(is_citizen, bool):
        return False
    return age >= 18 and is_citizen

if __name__ == '__main__':
    result1 = is_eligible_to_vote(20, True)
    print(result1)
    result2 = is_eligible_to_vote(16, True)
    print(result2)
    result3 = is_eligible_to_vote(25, False)
    print(result3)
    result4 = is_eligible_to_vote(-5, True)
    print(result4)
    result5 = is_eligible_to_vote(18, True)
    print(result5)