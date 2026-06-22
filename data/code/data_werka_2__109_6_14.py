from datetime import datetime, timedelta

def fraction_of_month_remaining(start_date: datetime, end_date: datetime) -> float:
    total_seconds = (end_date - start_date).total_seconds()
    if total_seconds <= 0:
        return 0.0
    now = datetime.now()
    if now < start_date:
        return 1.0
    if now > end_date:
        return 0.0
    elapsed_seconds = (now - start_date).total_seconds()
    return 1.0 - (elapsed_seconds / total_seconds)

if __name__ == '__main__':
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 31, 23, 59, 59)
    result = fraction_of_month_remaining(start, end)
    print(result)