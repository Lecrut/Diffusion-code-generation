def check_voting_eligibility():
    birth_year_string = "1995-06-15"
    birth_year = int(birth_year_string.split('-')[0])
    current_year = 2024
    age = current_year - birth_year
    if age >= 18:
        return True
    return False

if __name__ == '__main__':
    result = check_voting_eligibility()
    print(result)