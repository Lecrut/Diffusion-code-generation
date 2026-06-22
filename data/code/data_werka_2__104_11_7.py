from datetime import datetime, timedelta

def calculate_days_difference(start: datetime, end: datetime) -> int:
    delta = end - start
    return delta.days

if __name__ == '__main__':
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    result = calculate_days_difference(start_date, end_date)
    print(result)