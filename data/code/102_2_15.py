from datetime import date

WEEKDAY_THRESHOLD = 5
MONDAY_INDEX = 0
FRIDAY_INDEX = 4

def is_weekday(d: date) -> bool:
    day_of_week = d.weekday()
    return MONDAY_INDEX <= day_of_week <= FRIDAY_INDEX

if __name__ == '__main__':
    test_dates = [
        date(2023, 10, 23),
        date(2023, 10, 21),
        date(2023, 10, 22),
        date(2024, 1, 1)
    ]
    for d in test_dates:
        print(is_weekday(d))