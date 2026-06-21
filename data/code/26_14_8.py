VOTE_AGE = 1 << 0
VOTE_CITIZEN = 1 << 1
VOTE_DISFRANCHISED = 1 << 2

def is_eligible_to_vote(status_flags):
    eligible = (status_flags & VOTE_AGE) and (status_flags & VOTE_CITIZEN) and not (status_flags & VOTE_DISFRANCHISED)
    return eligible

def calculate_eligibility(age, is_citizen, is_disfranchised):
    flags = 0
    if age >= 18:
        flags |= VOTE_AGE
    if is_citizen:
        flags |= VOTE_CITIZEN
    if is_disfranchised:
        flags |= VOTE_DISFRANCHISED
    return is_eligible_to_vote(flags)

if __name__ == '__main__':
    result1 = calculate_eligibility(25, True, False)
    print(result1)
    result2 = calculate_eligibility(16, True, False)
    print(result2)
    result3 = calculate_eligibility(25, False, False)
    print(result3)
    result4 = calculate_eligibility(25, True, True)
    print(result4)
    result5 = calculate_eligibility(18, True, False)
    print(result5)
    result6 = calculate_eligibility(17, True, False)
    print(result6)