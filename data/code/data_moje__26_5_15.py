def check_voting_eligibility(ages):
    return ['Eligible' if age >= 18 else 'Ineligible' for age in ages]

if __name__ == '__main__':
    hard_coded_ages = [17, 18, 25, 16, 30, 18]
    results = check_voting_eligibility(hard_coded_ages)
    for result in results:
        print(result)