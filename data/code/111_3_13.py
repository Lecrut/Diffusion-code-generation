from datetime import date

MONTHS_IN_YEAR = 12
DAYS_IN_WEEK = 7

def subtract_months(target_date, months_to_subtract):
    total_months = target_date.year * MONTHS_IN_YEAR + target_date.month
    new_total_months = total_months - months_to_subtract
    new_year = new_total_months // MONTHS_IN_YEAR
    new_month = new_total_months % MONTHS_IN_YEAR
    if new_month == 0:
        new_month = MONTHS_IN_YEAR
        new_year -= 1
    days_in_new_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
        days_in_new_month[1] = 29
    max_day = days_in_new_month[new_month - 1]
    new_day = min(target_date.day, max_day)
    return date(new_year, new_month, new_day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)