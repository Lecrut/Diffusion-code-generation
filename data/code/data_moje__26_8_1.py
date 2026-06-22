def check_voting_eligibility(birth_year_string):
    birth_year = int(birth_year_string)
    current_year = 2024
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_birth_year = "2006"
    result = check_voting_eligibility(sample_birth_year)
    print(result)