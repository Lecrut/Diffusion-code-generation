from datetime import date

def is_weekday(d):
    return d.isoweekday() < 6

if __name__ == '__main__':
    check_dates = [
        date(2023, 10, 23),
        date(2023, 10, 21),
        date(2023, 10, 22),
        date(2024, 1, 1)
    ]
    for d in check_dates:
        print(is_weekday(d))