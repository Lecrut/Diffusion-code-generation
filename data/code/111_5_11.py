from datetime import date

def get_age_in_years(birth_date, current_date):
    if not isinstance(birth_date, date):
        raise ValueError("birth_date must be a date object")
    if not isinstance(current_date, date):
        raise ValueError("current_date must be a date object")
    if birth_date > current_date:
        raise ValueError("birth_date cannot be after current_date")
    age_years = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age_years -= 1
    return age_years

if __name__ == '__main__':
    person_birth = date(1990, 3, 15)
    today = date(2024, 1, 1)
    age = get_age_in_years(person_birth, today)
    print(age)