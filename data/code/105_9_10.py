from datetime import datetime, timedelta

def get_next_monday(reference_date: datetime) -> datetime:
    days_ahead = 0
    if reference_date.weekday() == 0:
        days_ahead = 7
    else:
        days_ahead = (0 - reference_date.weekday()) % 7
    return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    reference_date = datetime(2024, 2, 28)
    next_monday = get_next_monday(reference_date)
    print(next_monday.strftime("%Y-%m-%d"))