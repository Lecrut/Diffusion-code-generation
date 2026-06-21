def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return False
    if age < 0:
        return False
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    sample_ages = [17, 18, 19, -1, 0, 100, 17.9, 18.0]
    for age in sample_ages:
        print(check_voting_eligibility(age))