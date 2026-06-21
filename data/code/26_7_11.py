def filter_voting_eligible(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    ages = [16, 17, 18, 19, 20, 15, 25, 12]
    eligible_ages = filter_voting_eligible(ages)
    print(eligible_ages)