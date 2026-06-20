from datetime import date

def validate_dates(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of 'date'")
    return True

def days_between_dates(date1: date, date2: date) -> int:
    validate_dates(date1, date2)
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    sample_date1 = date(2023, 8, 1)
    sample_date2 = date(2023, 8, 15)
    print(days_between_dates(sample_date1, sample_date2))