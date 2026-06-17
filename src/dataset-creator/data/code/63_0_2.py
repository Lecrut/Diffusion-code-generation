import datetime
def subtract_years(date: datetime.date, years_to_subtract: int) -> datetime.date:
    year = date.year - years_to_subtract
    try:
        return datetime.date(year, date.month, date.day)
    except ValueError:
        if date.month == 2 and date.day == 29:
            return datetime.date(year, 2, 28) if not is_leap_year(year) else datetime.date(year + 1, 2, 28)
        raise
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 6, 15)
    years_to_subtract = 5
    result_date = subtract_years(sample_date, years_to_subtract)
    print(f"Original Date: {sample_date}")
    print(f"Subtracted Years: {years_to_subtract}")
    print(f"Resulting Date: {result_date}")