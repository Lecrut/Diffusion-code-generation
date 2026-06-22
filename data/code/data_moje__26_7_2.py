def get_eligible_voters(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidate_ages = [15, 17, 18, 19, 20, 16, 18]
    eligible_voters = get_eligible_voters(candidate_ages)
    print(eligible_voters)