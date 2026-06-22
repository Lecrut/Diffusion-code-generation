from datetime import date

def get_age_in_years(birth_date, current_date):
    if not isinstance(birth_date, date):
        raise ValueError("birth_date must be a date object")
    if not isinstance(current_date, date):
        raise ValueError("current_date must be a date object")
    if current_date < birth_date:
        raise ValueError("current_date cannot be before birth_date")
    years = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    current_date = date(2024, 1, 1)
    age = get_age_in_years(birth_date, current_date)
    print(age)