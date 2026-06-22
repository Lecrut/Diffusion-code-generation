from datetime import date

def is_weekend(dt: date) -> bool:
    return dt.weekday() >= 5

if __name__ == '__main__':
    dates = [date(2023, 10, 9), date(2023, 10, 10), date(2023, 10, 11)]
    results = {dt: is_weekend(dt) for dt in dates}
    print(results)