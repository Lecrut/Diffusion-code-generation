import datetime

TARGET_WEEKDAY_MONDAY = 0

def calculate_next_monday_date(reference_date: datetime.date) -> datetime.date:
    days_until_monday = (TARGET_WEEKDAY_MONDAY - reference_date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return reference_date + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    next_monday_date = calculate_next_monday_date(sample_date)
    print(next_monday_date)