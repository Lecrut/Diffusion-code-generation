def check_voting_eligibility(age):
    if not isinstance(age, int):
        return "Invalid input: age must be an integer"
    if age < 0:
        return "Invalid input: age cannot be negative"
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

if __name__ == '__main__':
    test_cases = [17, 18, 19, -5, 0, 100]
    for value in test_cases:
        result = check_voting_eligibility(value)
        print(f"Age: {value} -> {result}")