from datetime import date, timedelta

DAYS_TO_ADD = 30
TARGET_YEAR = 2024
TARGET_MONTH = 7
TARGET_DAY = 4
DATE_FORMAT = "%Y-%m-%d"

def add_days_to_specific_date():
    base = date(TARGET_YEAR, TARGET_MONTH, TARGET_DAY)
    delta = timedelta(days=DAYS_TO_ADD)
    new_date = base + delta
    return new_date.strftime(DATE_FORMAT)

if __name__ == '__main__':
    print(add_days_to_specific_date())