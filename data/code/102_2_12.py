from datetime import date

def is_weekday(d: date) -> bool:
    if not isinstance(d, date):
        raise ValueError("Input must be a datetime.date instance")
    if d.weekday() > 4:
        return False
    return True

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    print(is_weekday(test_date))
    print(is_weekday(date(2023, 10, 21)))