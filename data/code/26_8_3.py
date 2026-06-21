from datetime import datetime

def check_voting_eligibility(birth_info):
    birth_year = int(birth_info.split()[-1])
    current_year = datetime.now().year
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_birth_info = "John Doe born in 1990"
    eligible = check_voting_eligibility(sample_birth_info)
    print(eligible)