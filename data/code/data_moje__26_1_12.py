def check_voting_eligibility(age):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0:
        return "Invalid age: age cannot be negative"
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

if __name__ == '__main__':
    test_ages = [17, 18, 19, 0, -5, 100]
    for age_value in test_ages:
        result = check_voting_eligibility(age_value)
        print(f"Age {age_value}: {result}")