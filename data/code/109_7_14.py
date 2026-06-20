import datetime

DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12
SECONDS_PER_DAY = 86400

def get_last_day_of_month(year, month):
    if month == 12:
        return datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        return datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

def seconds_remaining_in_current_month():
    current_date = datetime.date.today()
    last_day_of_current_month = get_last_day_of_month(current_date.year, current_date.month)
    days_until_end_of_month = (last_day_of_current_month - current_date).days + 1
    return days_until_end_of_month * SECONDS_PER_DAY

if __name__ == '__main__':
    print(seconds_remaining_in_current_month())