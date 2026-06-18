from datetime import date, datetime
def subtract_years(d: datetime | date, years: int) -> datetime:
    if not isinstance(years, int):
        raise TypeError("The 'years' argument must be an integer.")
    if years < 0:
        raise ValueError("The number of years to subtract cannot be negative.")
    try:
        return d - timedelta(days=365 * years)
    except Exception as e:
        if isinstance(d, date):
            result_date = d.replace(year=d.year - years)
            return datetime.combine(result_date, datetime.min.time())
        else:
            raise
def subtract_years_safe(d: datetime | date, years: int) -> datetime:
    from datetime import timedelta
    if not isinstance(years, int):
        raise TypeError("The 'years' argument must be an integer.")
    if years < 0:
        raise ValueError("The number of years to subtract cannot be negative.")
    try:
        new_year = d.year - years
        if isinstance(d, datetime):
            temp_date = d.date().replace(year=new_year)
            result_datetime = datetime.combine(temp_date, d.time())
            try:
                return result_datetime.replace(day=365 % 4 + temp_date.day - 1 if not is_leap_year(new_year) else 0, hour=d.hour, minute=d.minute, second=d.second, microsecond=d.microsecond)
            except ValueError:
                import calendar
                days_in_month = len(calendar.monthcalendar(new_year, temp_date.strftime("%B")))
                if d.day > days_in_month:
                    target_day = min(d.day - 1, days_in_month)
                    return result_datetime.replace(day=target_day)
        else:
            return datetime.combine(temp_date.replace(year=new_year), datetime.min.time())
    except Exception as e:
        raise ValueError(f"Invalid date arithmetic for {d} and {years}")
def is_leap_year(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if __name__ == '__main__':
    sample_datetime = datetime(2023, 6, 15, 10, 30, 45)
    subtract_years(sample_datetime, 5)