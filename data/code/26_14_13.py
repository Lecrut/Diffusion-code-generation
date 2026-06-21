def check_voting_eligibility(age, is_citizen, is_disenfranchised):
    AGE_FLAG = 1 << 0
    CITIZEN_FLAG = 1 << 1
    DISFRANCHISED_FLAG = 1 << 2

    flags = 0
    if age >= 18:
        flags |= AGE_FLAG
    if is_citizen:
        flags |= CITIZEN_FLAG
    if is_disenfranchised:
        flags |= DISFRANCHISED_FLAG

    eligible = bool(flags & AGE_FLAG) and bool(flags & CITIZEN_FLAG) and not bool(flags & DISFRANCHISED_FLAG)
    return eligible

if __name__ == '__main__':
    result1 = check_voting_eligibility(20, True, False)
    result2 = check_voting_eligibility(16, True, False)
    result3 = check_voting_eligibility(25, False, False)
    result4 = check_voting_eligibility(30, True, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)