import datetime
from dateutil import parser as dt_parser
def subtract_years(date_obj: datetime.date, years: int) -> datetime.date:
    return date_obj.replace(year=date_obj.year - years)
if __name__ == '__main__':
    sample_date = "2023-12-31"
    years_to_subtract = 5
    try:
        parsed_date = dt_parser.parse(sample_date, dayfirst=True)
        result_date = subtract_years(parsed_date.date(), years_to_subtract)
        print(f"{sample_date} minus {years_to_subtract} years is {result_date}")
    except Exception as e:
        print(f"Error processing date: {e}")