from datetime import datetime

def calculate_age(birth_date_str, current_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == '__main__':
    birth_date = "1990-05-15"
    current_date = "2023-04-10"
    print(calculate_age(birth_date, current_date))