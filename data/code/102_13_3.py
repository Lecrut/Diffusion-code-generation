from datetime import date

def is_weekday(d: date) -> bool:
    return d.weekday() < 5

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 30),
        date(2023, 10, 31),
        date(2023, 11, 1),
    ]
    for d in sample_dates:
        print(is_weekday(d))