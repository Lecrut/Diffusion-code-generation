from datetime import date

WEEKDAY_MAP = {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: False,
    6: False,
}

def is_weekday(d: date) -> bool:
    return WEEKDAY_MAP[d.weekday()]

if __name__ == '__main__':
    test_dates = [
        date(2023, 10, 23),
        date(2023, 10, 28),
    ]
    for d in test_dates:
        print(is_weekday(d))