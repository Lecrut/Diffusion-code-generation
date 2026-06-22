def get_voting_status(age: int, threshold: int = 18) -> str:
    if age >= threshold:
        return "eligible"
    else:
        return "ineligible"

if __name__ == '__main__':
    result = get_voting_status(20)
    print(result)