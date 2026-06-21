def check_voting_eligibility(birth_year_string: str) -> bool:
    from datetime import datetime
    current_year = datetime.now().year
    try:
        birth_year = int(birth_year_string)
    except ValueError:
        return False
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_birth_year = "2005"
    result = check_voting_eligibility(sample_birth_year)
    print(result)