from datetime import date, datetime
def subtract_years(d: datetime | date, years: int) -> datetime:
    if isinstance(d, (datetime, date)) and isinstance(years, int):
        try:
            return d.replace(year=d.year - years)
        except ValueError as e:
            raise TypeError(f"Invalid input for subtraction: {e}") from e
    else:
        raise TypeError("Input types must be datetime/date and integer respectively.")
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    years_to_subtract = 5
    result = subtract_years(sample_date, years_to_subtract)
    print(result)