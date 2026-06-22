from datetime import date

def calculate_age_in_years(birth_date, current_date):
    if birth_date > current_date:
        raise ValueError("Birth date cannot be after current date")
    age = current_date.year - birth_date.year
    is_not_birthday_yet = (current_date.month, current_date.day) < (birth_date.month, birth_date.day)
    if is_not_birthday_yet:
        age -= 1
    return age

if __name__ == '__main__':
    birth = date(1990, 3, 15)
    today = date(2024, 1, 1)
    print(calculate_age_in_years(birth, today))