def get_voting_eligible_candidates(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidates_ages = [16, 17, 18, 19, 20, 15, 14]
    eligible = get_voting_eligible_candidates(candidates_ages)
    print(eligible)