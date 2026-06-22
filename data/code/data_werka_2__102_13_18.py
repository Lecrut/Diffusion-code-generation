from datetime import date, datetime

def is_weekday(d):
    if isinstance(d, date) and not isinstance(d, datetime):
        return d.weekday() < 5
    if isinstance(d, datetime):
        return d.weekday() < 5
    raise ValueError("Input must be a date or datetime object")

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    sample_weekend = date(2023, 10, 21)
    print(is_weekday(sample_date))
    print(is_weekday(sample_weekend))