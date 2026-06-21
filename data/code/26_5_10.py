def check_voting_eligibility(age):
    if age >= 18:
        return 'Eligible'
    return 'Ineligible'

if __name__ == '__main__':
    ages = [17, 18, 19, 25, 16, 65]
    results = [check_voting_eligibility(age) for age in ages]
    print(results)