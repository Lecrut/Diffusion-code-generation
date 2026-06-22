def filter_voting_ages(ages):
    return [age for age in ages if age >= 18]

if __name__ == '__main__':
    sample_ages = [16, 17, 18, 19, 20, 15, 25, 18]
    print(filter_voting_ages(sample_ages))