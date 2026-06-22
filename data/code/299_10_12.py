from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def is_weekend(year, month, day):
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date provided")
    target_date = date(year, month, day)
    return target_date.weekday() >= 5

if __name__ == '__main__':
    print(is_weekend(2023, 10, 7))
    print(is_weekend(2023, 10, 8))