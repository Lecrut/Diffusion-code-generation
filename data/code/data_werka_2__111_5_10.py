from datetime import date

BIRTH_DATE = date(1990, 3, 15)
CURRENT_DATE = date(2024, 1, 1)

AGE_RULES = {
    "adjustment": 1,
    "comparison_key": lambda d: (d.month, d.day)
}

def get_age_in_years(birth: date, now: date) -> int:
    base_age = now.year - birth.year
    birth_marker = AGE_RULES["comparison_key"](birth)
    current_marker = AGE_RULES["comparison_key"](now)
    if current_marker < birth_marker:
        return base_age - AGE_RULES["adjustment"]
    return base_age

if __name__ == '__main__':
    age = get_age_in_years(BIRTH_DATE, CURRENT_DATE)
    print(age)