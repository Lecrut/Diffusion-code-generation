def filter_eligible_voters(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    candidate_ages = [16, 17, 18, 19, 20, 45, 12, 30]
    eligible_ages = filter_eligible_voters(candidate_ages)
    print(eligible_ages)