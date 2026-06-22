from datetime import date

def is_valid_date(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    dates = ['2023-10-09', '2023-10-10', '2023-10-11']
    results = {}
    for date_str in dates:
        if is_valid_date(date_str):
            dt = date.fromisoformat(date_str)
            results[date_str] = is_weekend(dt)
        else:
            results[date_str] = False
    print(results)