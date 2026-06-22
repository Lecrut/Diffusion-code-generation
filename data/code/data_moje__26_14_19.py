AGE_FLAG = 1 << 0
CITIZENSHIP_FLAG = 1 << 1
DISENFRANCHISED_FLAG = 1 << 2

def calculate_voting_eligibility(age: int, is_citizen: bool, is_disenfranchised: bool) -> int:
    flags = 0
    if age >= 18:
        flags |= AGE_FLAG
    if is_citizen:
        flags |= CITIZENSHIP_FLAG
    if is_disenfranchised:
        flags |= DISENFRANCHISED_FLAG
    
    eligibility_mask = AGE_FLAG | CITIZENSHIP_FLAG
    return 1 if (flags & eligibility_mask) == eligibility_mask and not (flags & DISENFRANCHISED_FLAG) else 0

if __name__ == '__main__':
    sample_age_1 = 25
    sample_is_citizen_1 = True
    sample_is_disenfranchised_1 = False
    result_1 = calculate_voting_eligibility(sample_age_1, sample_is_citizen_1, sample_is_disenfranchised_1)
    print(result_1)

    sample_age_2 = 16
    sample_is_citizen_2 = True
    sample_is_disenfranchised_2 = False
    result_2 = calculate_voting_eligibility(sample_age_2, sample_is_citizen_2, sample_is_disenfranchised_2)
    print(result_2)

    sample_age_3 = 30
    sample_is_citizen_3 = True
    sample_is_disenfranchised_3 = True
    result_3 = calculate_voting_eligibility(sample_age_3, sample_is_citizen_3, sample_is_disenfranchised_3)
    print(result_3)

    sample_age_4 = 45
    sample_is_citizen_4 = False
    sample_is_disenfranchised_4 = False
    result_4 = calculate_voting_eligibility(sample_age_4, sample_is_citizen_4, sample_is_disenfranchised_4)
    print(result_4)