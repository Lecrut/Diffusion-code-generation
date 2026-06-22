from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

def validate_date(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    dates = ['2023-10-09', '2023-10-10', '2023-10-11']
    results = {date_str: is_weekend(date.fromisoformat(date_str)) if validate_date(date_str) else None for date_str in dates}
    print(results)