from datetime import date

DAYS_IN_MONTHS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def count_days_in_year(year):
    total_days = 0
    for month_days in DAYS_IN_MONTHS.values():
        total_days += month_days
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        total_days += 1
    return total_days

def calculate_days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    result = calculate_days_between(start, end)
    print(result)