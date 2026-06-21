def filter_voting_eligible_ages(ages):
    eligible_ages = []
    for age in ages:
        if age >= 18:
            eligible_ages.append(age)
    return eligible_ages

if __name__ == '__main__':
    sample_ages = [16, 18, 19, 20, 17, 25, 30, 15]
    result = filter_voting_eligible_ages(sample_ages)
    print(result)