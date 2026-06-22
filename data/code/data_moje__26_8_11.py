def is_voting_eligible(birth_year_string):
    try:
        birth_year = int(birth_year_string)
    except ValueError:
        return False
    current_year = 2024
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_birth_year = "2005"
    result = is_voting_eligible(sample_birth_year)
    print(result)
    sample_birth_year_2 = "2000"
    result_2 = is_voting_eligible(sample_birth_year_2)
    print(result_2)