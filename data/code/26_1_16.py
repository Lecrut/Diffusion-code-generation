def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return False
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    sample_ages = [17, 18, 20, -5, 0, 100, "not_a_number"]
    for age in sample_ages:
        if isinstance(age, (int, float)):
            result = check_voting_eligibility(age)
        else:
            result = check_voting_eligibility(age)
        print(result)