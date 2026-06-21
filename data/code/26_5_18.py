def check_voting_eligibility(age):
    if age >= 18:
        return 'Eligible'
    else:
        return 'Ineligible'

if __name__ == '__main__':
    ages = [16, 18, 20, 17, 25]
    for age in ages:
        result = check_voting_eligibility(age)
        print(f"Age: {age} -> {result}")