def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    sample_ages = [16, 18, 19, 17, 20, 10, 45]
    output = check_voting_eligibility(sample_ages)
    for item in output:
        print(item)