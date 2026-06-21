def check_voting_eligibility(age: int, citizenship: int, disenfranchised: int) -> bool:
    AGE_FLAG = 1
    CITIZENSHIP_FLAG = 2
    DISFRANCHISED_FLAG = 4

    is_adult = age >= 18
    is_citizen = bool(citizenship & CITIZENSHIP_FLAG)
    is_disfranchised = bool(disenfranchised & DISFRANCHISED_FLAG)

    eligible = is_adult and is_citizen and not is_disfranchised
    return eligible

if __name__ == '__main__':
    sample_age = 25
    sample_citizenship = 2
    sample_disfranchised = 0

    result = check_voting_eligibility(sample_age, sample_citizenship, sample_disfranchised)
    print(result)

    sample_age_underage = 16
    result_underage = check_voting_eligibility(sample_age_underage, sample_citizenship, sample_disfranchised)
    print(result_underage)

    sample_age_adult = 30
    sample_non_citizen = 0
    result_non_citizen = check_voting_eligibility(sample_age_adult, sample_non_citizen, sample_disfranchised)
    print(result_non_citizen)

    sample_disfranchised_person = 4
    result_disfranchised = check_voting_eligibility(sample_age_adult, sample_citizenship, sample_disfranchised_person)
    print(result_disfranchised)