def is_voting_eligible(age: int, citizen: bool, disenfranchised: bool) -> int:
    age_bit = 1 if age >= 18 else 0
    citizen_bit = 1 if citizen else 0
    disenfranchised_bit = 1 if disenfranchised else 0
    status_flags = age_bit << 2 | citizen_bit << 1 | disenfranchised_bit
    age_citizen_set = status_flags & 6 == 6
    disenfranchised_clear = status_flags & 1 == 0
    return 1 if age_citizen_set and disenfranchised_clear else 0
if __name__ == '__main__':
    result1 = is_voting_eligible(age=20, citizen=True, disenfranchised=False)
    print(result1)
    result2 = is_voting_eligible(age=16, citizen=True, disenfranchised=False)
    print(result2)
    result3 = is_voting_eligible(age=25, citizen=False, disenfranchised=False)
    print(result3)
    result4 = is_voting_eligible(age=30, citizen=True, disenfranchised=True)
    print(result4)
    result5 = is_voting_eligible(age=18, citizen=True, disenfranchised=False)
    print(result5)
    result6 = is_voting_eligible(age=21, citizen=False, disenfranchised=True)
    print(result6)