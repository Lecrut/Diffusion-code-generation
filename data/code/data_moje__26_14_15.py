def check_voting_eligibility(age, citizen, disenfranchised):
    if age < 18:
        return False
    if not citizen:
        return False
    if disenfranchised:
        return False
    return True

def check_voting_eligibility_bitwise(age, citizen, disenfranchised):
    status_flags = 0
    if age >= 18:
        status_flags |= 1
    if citizen:
        status_flags |= 2
    if not disenfranchised:
        status_flags |= 4
    return (status_flags & 7) == 7

if __name__ == '__main__':
    result1 = check_voting_eligibility_bitwise(20, True, False)
    print(result1)
    result2 = check_voting_eligibility_bitwise(16, True, False)
    print(result2)
    result3 = check_voting_eligibility_bitwise(25, False, False)
    print(result3)
    result4 = check_voting_eligibility_bitwise(30, True, True)
    print(result4)