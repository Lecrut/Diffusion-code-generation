import datetime

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_days_remaining(target_month, current_month):
    if target_month > current_month:
        days = DAYS_IN_MONTH[current_month]
        if is_leap_year(datetime.date.today().year) and current_month == 2:
            days += 1
        return days - datetime.date.today().day
    else:
        return (datetime.date(datetime.date.today().year, target_month + 1, 1) - datetime.date(datetime.date.today().year, target_month, 1)).days

if __name__ == '__main__':
    sample_month = 12
    days_left = calculate_days_remaining(sample_month, datetime.date.today().month)
    print(days_left)