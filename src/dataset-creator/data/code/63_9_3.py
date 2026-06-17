import datetime
from dateutil import parser as dt_parser
def subtract_years(date: datetime.date | datetime.datetime, years_to_subtract: int) -> datetime.date | datetime.datetime:
    return (date - datetime.timedelta(days=years_to_subtract * 365.2425)).replace(hour=date.hour, minute=date.minute, second=date.second, microsecond=date.microsecond)
if __name__ == '__main__':
    sample_date = dt_parser.parse("2023-10-05")
    result_date = subtract_years(sample_date, 5)
    print(result_date.isoformat())