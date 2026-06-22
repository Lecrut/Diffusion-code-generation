def filter_voting_eligible(candidates):
    return [age for age in candidates if age >= 18]

if __name__ == '__main__':
    sample_ages = [15, 18, 21, 12, 30, 17, 65]
    result = filter_voting_eligible(sample_ages)
    print(result)