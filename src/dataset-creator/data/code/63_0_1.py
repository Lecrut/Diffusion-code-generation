from datetime import date
def subtract_years(original_date: date, years_to_subtract: int) -> date:
    year = original_date.year - years_to_subtract
    try:
        new_date = date(year, original_date.month, original_date.day)
    except ValueError:
        if original_date.month == 1 and original_date.day != 31 or\
           original_date.month > 1 and not is_leap_year(year):
            last_day_of_february = date(year, 2, 28).day
            new_date = date(year, 2, last_day_of_february)
        else:
            if original_date.day == 31 and not is_leap_year(year):
                days_in_last_month = date(year, original_date.month - 1, None).day
            else:
                 new_date = date(year, original_date.month, min(original_date.day, date(year, original_date.month, None).day))
    return new_date
def is_leap_year(y) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if __name__ == '__main__':
    sample_date = date(2023, 5, 31)
    years_to_subtract = 1
    result_date = subtract_years(sample_date, years_to_subtract)
    print(f"Original Date: {sample_date}")
    print(f"Years to Subtract: {years_to_subtract}")
    print(f"Resulting Date: {result_date}")