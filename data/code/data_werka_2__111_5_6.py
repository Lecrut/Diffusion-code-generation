from datetime import date

def compute_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    birth_date = date(birth_year, birth_month, birth_day)
    current_date = date(current_year, current_month, current_day)
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

if __name__ == '__main__':
    result = compute_age(1990, 3, 15, 2024, 1, 1)
    print(result)