import datetime

def _validate_date(date_val: datetime.date, name: str) -> datetime.date:
    if not isinstance(date_val, datetime.date):
        raise ValueError(f"{name} must be a datetime.date instance")
    return date_val

def is_same_week(date1: datetime.date, date2: datetime.date) -> bool:
    valid_d1 = _validate_date(date1, "date1")
    valid_d2 = _validate_date(date2, "date2")
    iso_d1 = valid_d1.isocalendar()
    iso_d2 = valid_d2.isocalendar()
    return iso_d1[0] == iso_d2[0] and iso_d1[1] == iso_d2[1]

if __name__ == '__main__':
    dt_jan1 = datetime.date(2024, 1, 1)
    dt_jan7 = datetime.date(2024, 1, 7)
    dt_jan8 = datetime.date(2024, 1, 8)
    dt_dec31 = datetime.date(2023, 12, 31)
    print(is_same_week(dt_jan1, dt_jan7))
    print(is_same_week(dt_jan1, dt_jan8))
    print(is_same_week(dt_dec31, dt_jan1))