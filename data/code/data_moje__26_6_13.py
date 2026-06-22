def validate_voting_eligibility(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    test_ages = [17, 18, 19, 25, 100, -1]
    for age in test_ages:
        try:
            result = validate_voting_eligibility(age)
            print(f"Age {age}: {result}")
        except ValueError as e:
            print(f"Age {age}: Error - {e}")