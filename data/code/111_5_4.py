from datetime import date

BIRTH_DATE = date(1990, 3, 15)
CURRENT_DATE = date(2024, 1, 1)

AGE_CALCULATION_RULES = {
    "year_diff": 1,
    "birthday_check": lambda current, birth: (current.month, current.day) < (birth.month, birth.day)
}

def calculate_age(birth_date, current_date):
    year_difference = current_date.year - birth_date.year
    is_birthday_passed = not AGE_CALCULATION_RULES["birthday_check"](current_date, birth_date)
    
    if is_birthday_passed:
        return year_difference
    return year_difference - AGE_CALCULATION_RULES["year_diff"]

if __name__ == '__main__':
    age = calculate_age(BIRTH_DATE, CURRENT_DATE)
    print(age)