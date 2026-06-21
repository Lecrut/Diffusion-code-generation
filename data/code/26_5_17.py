def check_voting_eligibility(ages):
    return ['Eligible' if age >= 18 else 'Ineligible' for age in ages]

if __name__ == '__main__':
    ages = [15, 18, 21, 17, 30]
    result = check_voting_eligibility(ages)
    for status in result:
        print(status)