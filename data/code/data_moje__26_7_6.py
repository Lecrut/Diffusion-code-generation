def filter_voting_eligible(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidate_ages = [16, 17, 18, 19, 20, 21, 25, 30, 15]
    eligible_voters = filter_voting_eligible(candidate_ages)
    print(eligible_voters)