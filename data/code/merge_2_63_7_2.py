import datetime
from dateutil.relativedelta import relativedelta
def subtract_years_from_date(date_obj: datetime.date, years_to_subtract: int) -> str:
    new_date = date_obj - relativedelta(years=years_to_subtract)
    return new_date.isoformat()
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 5, 17),
        datetime.datetime(2024, 8, 9).date(),
        datetime.date(2020, 12, 31)
    ]
    years_to_subtract = 5
    for date in sample_dates:
        result_date_str = subtract_years_from_date(date, years_to_subtract)
        print(f"Original Date (ISO): {date.isoformat()}")
        print(f"After Subtracting {years_to_subtract} Years: {result_date_str}")
        print("-" * 40)