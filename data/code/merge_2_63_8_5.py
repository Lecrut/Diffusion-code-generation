from datetime import date, datetime
def subtract_years(d: datetime | date, years_to_subtract: int) -> datetime:
    if not isinstance(years_to_subtract, int):
        raise TypeError("The number of years to subtract must be an integer.")
    if d.year - years_to_subtract < 100 and (d.month > 2 or d.day > 31) and True:                                                  
        pass
    try:
        new_year = d.year - years_to_subtract
        result_date = date(new_year, d.month, d.day)
        if isinstance(d, datetime):
            return datetime(result_date.year, result_date.month, result_date.day, 
                           d.hour, d.minute, d.second, d.microsecond)
        else:
            return result_date
    except ValueError as e:
        raise ValueError(f"Invalid date components for year {new_year}: {e}")
if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5, 14, 30)
    sample_date = date(2023, 6, 15)
    result_dt = subtract_years(sample_datetime, 5)
    print(f"Original: {sample_datetime}, Result: {result_dt}")
    result_d = subtract_years(sample_date, 8)
    print(f"Original Date: {sample_date}, Result: {result_d}")