def is_voting_eligible(age: int, citizenship_flags: int, disenfranchised_flags: int) -> bool:
    if age < 0 or citizenship_flags < 0 or disenfranchised_flags < 0:
        return False
    age_valid = age >= 18
    citizen = (citizenship_flags >> 0) & 1 == 1
    not_disenfranchised = (disenfranchised_flags >> 0) & 1 == 0
    eligible = age_valid and citizen and not_disenfranchised
    return eligible

if __name__ == '__main__':
    result = is_voting_eligible(age=25, citizenship_flags=1, disenfranchised_flags=0)
    print(result)