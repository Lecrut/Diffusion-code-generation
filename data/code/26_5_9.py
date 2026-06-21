def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible"
    return "Ineligible"

if __name__ == '__main__':
    sample_ages = [17, 18, 25, 65]
    for age in sample_ages:
        result = check_voting_eligibility(age)
        print(f"Age {age}: {result}")