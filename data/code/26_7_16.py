def filter_eligible_voters(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    sample_ages = [16, 18, 19, 20, 17, 21, 10, 30]
    eligible_voters = filter_eligible_voters(sample_ages)
    print(eligible_voters)