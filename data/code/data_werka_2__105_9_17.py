from datetime import datetime, timedelta

def get_next_monday(reference_date: datetime) -> datetime:
    days_ahead = 7 - reference_date.weekday()
    if days_ahead == 0:
        days_ahead = 7
    next_monday = reference_date + timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    hard_coded_date = datetime(2024, 2, 28)
    result = get_next_monday(hard_coded_date)
    print(result)