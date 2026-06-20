from datetime import date
CURRENT_YEAR = 2024

def calculate_age(birth_date):
    if not isinstance(birth_date, date):
        raise ValueError('Input must be a date object.')
    today = date(CURRENT_YEAR, 1, 1)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    age = calculate_age(birth_date)
    print(age)