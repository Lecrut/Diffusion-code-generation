def check_voting_status(age: int, threshold: int = 18) -> bool:
    if age is None:
        return False
    return age >= threshold

if __name__ == '__main__':
    result = check_voting_status(20)
    print(result)