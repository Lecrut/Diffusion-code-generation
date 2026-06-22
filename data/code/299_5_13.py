from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    dates = [
        date(2023, 10, 9),
        date(2023, 10, 10),
        date(2023, 10, 11)
    ]
    for dt in dates:
        print(f"Is {dt} a weekend? {is_weekend(dt)}")