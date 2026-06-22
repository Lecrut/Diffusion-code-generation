def filter_voting_eligible_ages(ages):
    result = []
    for age in ages:
        if age >= 18:
            result.append(age)
    return result

if __name__ == '__main__':
    sample_ages = [16, 18, 20, 17, 25, 30, 15]
    eligible_ages = filter_voting_eligible_ages(sample_ages)
    print(eligible_ages)