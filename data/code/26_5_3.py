def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    sample_ages = [15, 18, 21, 12, 30]
    eligibility_results = check_voting_eligibility(sample_ages)
    for result in eligibility_results:
        print(result)