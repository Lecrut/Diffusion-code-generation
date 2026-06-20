from datetime import date

def calculate_age(birth_date):
    today = date(2024, 1, 1)
    if not isinstance(birth_date, date) or birth_date > today:
        raise ValueError("Invalid birth date")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    print(calculate_age(birth_date))