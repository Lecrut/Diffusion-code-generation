def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    ages = [16, 18, 25, 17, 21]
    outcome = check_voting_eligibility(ages)
    for item in outcome:
        print(item)