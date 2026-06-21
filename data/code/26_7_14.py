def filter_eligible_voters(ages):
    result = []
    for age in ages:
        if age >= 18:
            result.append(age)
    return result

if __name__ == '__main__':
    candidate_ages = [16, 17, 18, 19, 20, 15, 25, 30]
    eligible_voters = filter_eligible_voters(candidate_ages)
    print(eligible_voters)