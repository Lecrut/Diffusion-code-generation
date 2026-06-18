import datetime
from dateutil.relativedelta import relativedelta
def subtract_years_from_date(date_obj: datetime.date, years_to_subtract: int) -> str:
    new_date = date_obj - relativedelta(years=years_to_subtract)
    return new_date.isoformat()
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 5, 17),
        datetime.date(2024, 12, 31),
        datetime.date(2020, 6, 1)
    ]
    years_to_subtract_list = [-1, -5, -10]
    for date in sample_dates:
        print(f"Original Date (ISO): {date.isoformat()}")
        for y in years_to_subtract_list:
            result_date = subtract_years_from_date(date, y)
            print(f"After Subtracting {y} Years: {result_date}")