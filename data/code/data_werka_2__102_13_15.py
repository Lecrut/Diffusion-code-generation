from datetime import date, timedelta

def is_weekday(d: date) -> bool:
    if d.weekday() == 5 or d.weekday() == 6:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
        date(2023, 11, 1),
    ]
    for d in test_cases:
        print(is_weekday(d))