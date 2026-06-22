from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    dates_str = ['2023-10-09', '2023-10-10', '2023-10-11']
    date_map = {date.fromisoformat(date_str): date_str for date_str in dates_str}
    results = {date_str: is_weekend(dt) for dt, date_str in date_map.items()}
    print(results)