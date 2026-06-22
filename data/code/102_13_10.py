from datetime import date

def is_business_day(target: date) -> bool:
    if not isinstance(target, date):
        raise TypeError("Expected a datetime.date instance")
    day_index = target.weekday()
    return day_index < 5

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]
    for d in test_cases:
        print(is_business_day(d))