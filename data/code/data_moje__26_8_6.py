from datetime import datetime

def check_voting_eligibility(birth_year_str):
    birth_year = int(birth_year_str)
    current_year = datetime.now().year
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    birth_year_sample = "1990"
    is_eligible = check_voting_eligibility(birth_year_sample)
    print(is_eligible)