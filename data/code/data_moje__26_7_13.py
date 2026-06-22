def get_voting_eligible_ages(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidates = [16, 18, 20, 17, 25, 12, 30, 15, 19]
    eligible_ages = get_voting_eligible_ages(candidates)
    print(eligible_ages)