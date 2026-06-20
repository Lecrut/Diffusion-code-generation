from datetime import date

def calculate_age(birth_date):
    today = date(2024, 1, 1)
    if birth_date >= today:
        raise ValueError('Birth date must be earlier than the current date.')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    result = calculate_age(birth_date)
    print(result)