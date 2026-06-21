def get_eligible_candidates(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    sample_ages = [16, 17, 18, 19, 25, 15, 30]
    eligible = get_eligible_candidates(sample_ages)
    print(eligible)