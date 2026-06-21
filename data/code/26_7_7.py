def get_eligible_voters(ages):
    eligible_ages = []
    for age in ages:
        if age >= 18:
            eligible_ages.append(age)
    return eligible_ages

if __name__ == '__main__':
    sample_ages = [16, 18, 21, 17, 25, 30, 15, 19]
    result = get_eligible_voters(sample_ages)
    print(result)