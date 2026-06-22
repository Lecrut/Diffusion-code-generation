from datetime import date
from dateutil.relativedelta import relativedelta

BIRTH_DATE = date(1990, 3, 15)
CURRENT_DATE = date(2024, 1, 1)
BORN_CONSTANT = relativedelta(1990, 3, 15)

def compute_age_years(birth: date, current: date):
    delta = relativedelta(current, birth)
    return delta.years

if __name__ == '__main__':
    age = compute_age_years(BIRTH_DATE, CURRENT_DATE)
    print(age)