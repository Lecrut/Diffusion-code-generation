MINIMUM_VOTING_AGE = 18

def is_eligible_to_vote(age: int) -> bool:
    meets_age_requirement = age >= MINIMUM_VOTING_AGE
    return meets_age_requirement

if __name__ == '__main__':
    candidate_ages = [16, 18, 30, 65, 100]
    for age in candidate_ages:
        is_voter = is_eligible_to_vote(age)
        print(is_voter)