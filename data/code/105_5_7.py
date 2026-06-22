from datetime import datetime, timedelta

def next_wednesday(start_date: datetime) -> datetime:
    days_ahead = 2 - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    start = datetime(2023, 10, 10)
    result = next_wednesday(start)
    print(result)