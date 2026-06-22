def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return False
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    test_cases = [20, 17, 18, -5, 0, 18.0]
    for age in test_cases:
        print(check_voting_eligibility(age))