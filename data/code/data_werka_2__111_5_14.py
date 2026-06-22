from datetime import date

def get_age_in_years():
    BIRTH_DATE = date(1990, 3, 15)
    CURRENT_DATE = date(2024, 1, 1)
    year_diff = CURRENT_DATE.year - BIRTH_DATE.year
    month_day_compare = (CURRENT_DATE.month, CURRENT_DATE.day) < (BIRTH_DATE.month, BIRTH_DATE.day)
    age_adjustments = {True: -1, False: 0}
    return year_diff + age_adjustments[month_day_compare]

if __name__ == '__main__':
    print(get_age_in_years())