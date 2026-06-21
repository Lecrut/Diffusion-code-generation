def is_voting_eligible(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append('Eligible')
        else:
            results.append('Ineligible')
    return results

if __name__ == '__main__':
    ages = [16, 20, 17, 25]
    result = is_voting_eligible(ages)
    for status in result:
        print(status)