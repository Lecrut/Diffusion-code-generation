from datetime import date

def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def is_weekend(day):
    if not isinstance(day, date):
        raise TypeError('Input must be a date object')
    return day.weekday() >= 5
if __name__ == '__main__':
    sample_date1 = date(2023, 10, 21)
    print(is_weekend(sample_date1))
    sample_date2 = date(2023, 10, 22)
    print(is_weekend(sample_date2))
    sample_date3 = date(2023, 9, 16)
    print(is_weekend(sample_date3))