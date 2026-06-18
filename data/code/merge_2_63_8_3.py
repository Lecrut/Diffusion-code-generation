from datetime import date, datetime
def subtract_years(d: datetime | date, years: int) -> datetime | date:
    try:
        year = d.year - abs(years)
        month = d.month
        day = d.day
        new_date_obj = type(d)(year, month, day)
        return new_date_obj if isinstance(new_date_obj, date) else datetime.combine(date(year, month, day), time(0, 0))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid input: {d} or invalid years value.")
def subtract_years_safe(d: datetime | date, years: int) -> datetime | date:
    try:
        year = d.year - abs(years)
        month = d.month
        day = d.day
        new_date_obj = type(d)(year, month, day)
        return new_date_obj if isinstance(new_date_obj, date) else datetime.combine(date(year, month, day), time(0, 0))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid input: {d} or invalid years value.")
if __name__ == '__main__':
    from datetime import timedelta
    sample_date = date(2023, 10, 5)
    result = subtract_years(sample_date, 5)
    print(result)