def check_voting_eligibility(age):
    if age >= 18:
        return 'Eligible'
    return 'Ineligible'

if __name__ == '__main__':
    ages = [17, 18, 21, 5, 30, 18]
    for age in ages:
        print(check_voting_eligibility(age))