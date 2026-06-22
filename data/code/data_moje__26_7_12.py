def get_eligible_voters(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidates_ages = [15, 17, 18, 20, 16, 19, 18, 10]
    eligible_voters = get_eligible_voters(candidates_ages)
    print(eligible_voters)