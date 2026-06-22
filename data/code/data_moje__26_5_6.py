def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    ages = [15, 18, 21, 16, 30]
    eligible_statuses = check_voting_eligibility(ages)
    for status in eligible_statuses:
        print(status)