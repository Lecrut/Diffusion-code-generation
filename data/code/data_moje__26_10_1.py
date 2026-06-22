def is_voting_eligible(age: int, is_citizen: bool) -> bool:
    if not isinstance(age, int):
        return False
    if age < 0:
        return False
    if age < 18:
        return False
    if not is_citizen:
        return False
    return True

if __name__ == '__main__':
    result = is_voting_eligible(20, True)
    print(result)