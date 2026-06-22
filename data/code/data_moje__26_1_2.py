def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18

if __name__ == '__main__':
    test_cases = [17, 18, 25, -5, 0, 100, 17.9, 18.0]
    results = []
    for case in test_cases:
        try:
            result = check_voting_eligibility(case)
            results.append((case, result))
        except (TypeError, ValueError) as e:
            results.append((case, str(e)))
    for age, outcome in results:
        print(outcome)