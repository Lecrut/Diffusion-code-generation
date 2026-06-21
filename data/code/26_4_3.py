def get_voting_status(age: int, threshold: int=18) -> bool:
    return age >= threshold
if __name__ == '__main__':
    result = get_voting_status(20)
    print(result)
    result_threshold = get_voting_status(16, threshold=18)
    print(result_threshold)
    result_custom = get_voting_status(18, threshold=18)
    print(result_custom)