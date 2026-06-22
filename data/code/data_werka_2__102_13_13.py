from datetime import date, datetime

def is_weekday(d):
    if isinstance(d, datetime):
        return d.weekday() < 5
    if isinstance(d, date):
        return d.weekday() < 5
    raise ValueError("Unsupported input type")

if __name__ == '__main__':
    print(is_weekday(date(2023, 10, 23)))
    print(is_weekday(date(2023, 10, 21)))
    print(is_weekday(datetime(2023, 10, 23, 12, 0)))