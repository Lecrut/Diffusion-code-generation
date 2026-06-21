import datetime

def is_voting_eligible(birth_string: str) -> bool:
    year = int(birth_string.split(" ")[-1])
    current_year = datetime.date.today().year
    age = current_year - year
    return age >= 18

if __name__ == '__main__':
    result = is_voting_eligible("John Doe was born in 2005")
    print(result)