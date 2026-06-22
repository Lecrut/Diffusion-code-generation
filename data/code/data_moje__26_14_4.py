def check_voting_eligibility(age: int, citizenship: int, disenfranchised: int) -> int:
    return (age >= 18) and citizenship and (not disenfranchised)

if __name__ == '__main__':
    sample_cases = [
        (25, 1, 0),
        (16, 1, 0),
        (30, 0, 0),
        (40, 1, 1),
        (18, 1, 0)
    ]
    for age, citizenship, disenfranchised in sample_cases:
        eligible = check_voting_eligibility(age, citizenship, disenfranchised)
        print(int(eligible))