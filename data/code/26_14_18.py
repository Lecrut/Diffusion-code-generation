def check_voting_eligibility(age: int, citizenship_status: int, disenfranchised_status: int) -> bool:
    MIN_AGE = 18
    IS_CITIZEN = 1
    CITIZENSHIP_CHECK = citizenship_status & IS_CITIZEN
    IS_DISFRANCHISED = 1
    DISFRANCHISED_CHECK = disenfranchised_status & IS_DISFRANCHISED
    return age >= MIN_AGE and CITIZENSHIP_CHECK != 0 and (DISFRANCHISED_CHECK == 0)
if __name__ == '__main__':
    AGE = 20
    CITIZENSHIP_STATUS = 1
    DISFRANCHISED_STATUS = 0
    is_eligible = check_voting_eligibility(AGE, CITIZENSHIP_STATUS, DISFRANCHISED_STATUS)
    print(is_eligible)