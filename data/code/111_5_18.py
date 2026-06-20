import datetime

def calculate_age(birth_date):
    today = datetime.date(2024, 1, 1)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == '__main__':
    birth_date = datetime.date(1990, 3, 15)
    result = calculate_age(birth_date)
    print(result)