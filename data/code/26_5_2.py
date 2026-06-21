def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible"
    return "Ineligible"

if __name__ == '__main__':
    ages = [15, 18, 20, 17, 45]
    results = [check_voting_eligibility(age) for age in ages]
    for result in results:
        print(result)