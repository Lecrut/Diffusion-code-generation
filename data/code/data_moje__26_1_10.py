def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    sample_ages = [25, 17, 0, -5, 18, 100]
    results = []
    for age in sample_ages:
        try:
            result = check_voting_eligibility(age)
            results.append((age, result))
        except (TypeError, ValueError) as e:
            results.append((age, str(e)))
    for age, result in results:
        print(f"{age}: {result}")