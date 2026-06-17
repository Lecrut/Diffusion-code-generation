import datetime
def subtract_years(date_obj: datetime.date, years_to_subtract: int) -> datetime.date:
    try:
        new_date = date_obj.replace(year=date_obj.year - years_to_subtract)
        return new_date
    except ValueError as e:
        raise ValueError(f"Error subtracting {years_to_subtract} years: {e}")
if __name__ == '__main__':
    sample_date = datetime.date(2023, 6, 15)
    years_to_remove = 4
    result_date = subtract_years(sample_date, years_to_remove)
    print(f"Original Date: {sample_date.strftime('%Y-%m-%d')}")
    print(f"After Subtracting {years_to_remove} Years: {result_date.strftime('%Y-%m-%d')}")