def calculate_voting_eligibility(age: int, citizenship: bool, disenfranchised: bool) -> bool:
    if age < 18:
        return False
    if not citizenship:
        return False
    if disenfranchised:
        return False
    return True

def calculate_voting_eligibility_bitwise(age: int, citizenship: bool, disenfranchised: bool) -> bool:
    age_flag = 1 if age >= 18 else 0
    citizenship_flag = 1 if citizenship else 0
    disenfranchised_flag = 1 if not disenfranchised else 0
    status = age_flag | citizenship_flag | disenfranchised_flag
    return status == 7

if __name__ == '__main__':
    sample_cases = [
        (25, True, False),
        (17, True, False),
        (30, False, False),
        (40, True, True),
        (18, True, False),
    ]
    for age, citizenship, disenfranchised in sample_cases:
        result = calculate_voting_eligibility_bitwise(age, citizenship, disenfranchised)
        print(result)