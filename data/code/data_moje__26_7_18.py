def filter_voting_eligible(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    sample_ages = [15, 18, 21, 17, 30, 12, 18, 45]
    eligible_ages = filter_voting_eligible(sample_ages)
    print(eligible_ages)