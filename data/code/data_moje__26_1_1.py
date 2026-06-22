def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    test_cases = [25, 17, 18, 0, -5, 100]
    results = []
    for age in test_cases:
        try:
            result = check_voting_eligibility(age)
            results.append(result)
        except (TypeError, ValueError) as e:
            results.append(str(e))
    for result in results:
        print(result)