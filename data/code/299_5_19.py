from datetime import date
WEEKEND_DAYS = (5, 6)

def is_weekend(dt: date) -> bool:
    return dt.weekday() in WEEKEND_DAYS
if __name__ == '__main__':
    dates = [date(2023, 10, 9), date(2023, 10, 10), date(2023, 10, 11)]
    results = {str(date): is_weekend(date) for date in dates}
    print(results)