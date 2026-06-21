import datetime

def check_voting_eligibility(birth_year_str):
    birth_year = int(birth_year_str)
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_birth_year_str = "2000"
    is_eligible = check_voting_eligibility(sample_birth_year_str)
    print(is_eligible)