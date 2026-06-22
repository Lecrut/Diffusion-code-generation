def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    if age < 0:
        return False
    if age < 18:
        return False
    return True

if __name__ == '__main__':
    sample_ages = [17, 18, 19, -5, 25.5]
    for age in sample_ages:
        result = check_voting_eligibility(age)
        print(result)