from datetime import datetime

def calculate_age(birthdate_str, current_date_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age

if __name__ == '__main__':
    print(calculate_age("1990-05-15", "2023-04-30"))