from datetime import date

def validate_birth_date(birth_date):
    if birth_date > date.today():
        raise ValueError("Birth date cannot be in the future.")

def calculate_age(birth_date):
    today = date(2024, 1, 1)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    validate_birth_date(birth_date)
    print(calculate_age(birth_date))