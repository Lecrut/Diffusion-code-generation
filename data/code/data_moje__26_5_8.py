def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    ages = [17, 18, 25, 15, 30]
    results = check_voting_eligibility(ages)
    for result in results:
        print(result)