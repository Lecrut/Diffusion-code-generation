import datetime
from dateutil.relativedelta import relativedelta
def subtract_years(date_obj: datetime.date, years_to_subtract: int) -> datetime.date:
    return date_obj - relativedelta(years=years_to_subtract)
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 12, 31).date()
    result = subtract_years(sample_date, 5)
    print(result)