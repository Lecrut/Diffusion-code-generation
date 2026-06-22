from datetime import datetime, timedelta

WEEKDAY_MONDAY = 0
DAYS_IN_WEEK = 7

def compute_next_monday(reference: datetime) -> datetime:
    current_weekday = reference.weekday()
    days_offset = (WEEKDAY_MONDAY - current_weekday) % DAYS_IN_WEEK
    if days_offset == 0:
        days_offset = DAYS_IN_WEEK
    return reference + timedelta(days=days_offset)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    next_monday = compute_next_monday(sample_date)
    print(next_monday.strftime("%Y-%m-%d"))