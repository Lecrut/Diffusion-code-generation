from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    dates = [
        (date(2023, 10, 9), '2023-10-09'),
        (date(2023, 10, 10), '2023-10-10'),
        (date(2023, 10, 11), '2023-10-11')
    ]
    results = {date_str: is_weekend(dt) for dt, date_str in dates}
    print(results)