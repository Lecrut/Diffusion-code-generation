def is_voting_eligible(age):
    if age < 0:
        return False
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    test_ages = [17, 18, 19, -1, 100]
    results = []
    for age in test_ages:
        result = is_voting_eligible(age)
        results.append(result)
    print(results)