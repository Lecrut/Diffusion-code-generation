import datetime

DAY_NAMES = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

TARGET_YEAR = 2024
TARGET_MONTH = 1
TARGET_DAY = 1
TARGET_WEEKDAY = 6

def find_first_sunday_after_reference_date(year, month, day):
    base = datetime.date(year, month, day)
    current = base + datetime.timedelta(days=1)
    while current.weekday() != TARGET_WEEKDAY:
        current += datetime.timedelta(days=1)
    return current

if __name__ == '__main__':
    result = find_first_sunday_after_reference_date(TARGET_YEAR, TARGET_MONTH, TARGET_DAY)
    print(result)