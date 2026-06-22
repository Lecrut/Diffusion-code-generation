import datetime

WEEKDAY_SUNDAY = 6
START_YEAR = 2024
START_MONTH = 1
START_DAY = 1
DAYS_IN_WEEK = 7

def get_first_sunday_after_jan_1_2024():
    base = datetime.date(START_YEAR, START_MONTH, START_DAY)
    days_to_add = (WEEKDAY_SUNDAY - base.weekday()) % DAYS_IN_WEEK
    if days_to_add == 0:
        days_to_add = DAYS_IN_WEEK
    return base + datetime.timedelta(days=days_to_add)

if __name__ == '__main__':
    result = get_first_sunday_after_jan_1_2024()
    print(result)