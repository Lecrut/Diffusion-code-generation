from datetime import datetime, timedelta

FRIDAY_WEEKDAY = 4
DAY_DURATION = timedelta(days=1)
REFERENCE_DATE = datetime(2023, 12, 15)

def calculate_next_friday(reference: datetime) -> datetime:
    current_weekday = reference.weekday()
    days_difference = FRIDAY_WEEKDAY - current_weekday
    if days_difference <= 0:
        days_difference += 7
    return reference + DAY_DURATION * days_difference

if __name__ == '__main__':
    ref_date = REFERENCE_DATE
    next_friday = calculate_next_friday(ref_date)
    print(next_friday.strftime('%Y-%m-%d'))