import datetime

DAYS_IN_WEEK = 7
MONDAY_WEEKDAY = 0

def calculate_next_monday(reference_date: datetime.date) -> datetime.date:
    days_until_monday = (MONDAY_WEEKDAY - reference_date.weekday()) % DAYS_IN_WEEK
    if days_until_monday == 0:
        days_until_monday = DAYS_IN_WEEK
    return reference_date + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    next_monday = calculate_next_monday(sample_date)
    print(next_monday)