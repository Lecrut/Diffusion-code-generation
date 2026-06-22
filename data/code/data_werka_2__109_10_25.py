import datetime

DAYS_IN_MONTHS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(year, month):
    if month not in DAYS_IN_MONTHS:
        raise ValueError("Invalid month")
    if month == 2 and is_leap_year(year):
        return 29
    return DAYS_IN_MONTHS[month]

def calculate_days_remaining(year, month, day):
    target_date = datetime.date(year, month, day)
    days_in_current_month = get_days_in_month(year, month)
    days_passed = day - 1
    total_days = days_in_current_month
    remaining = total_days - days_passed
    return remaining

if __name__ == '__main__':
    samples = [
        (2023, 10, 15),
        (2024, 2, 29),
        (2023, 12, 31),
        (2023, 2, 28)
    ]
    for y, m, d in samples:
        result = calculate_days_remaining(y, m, d)
        print(result)