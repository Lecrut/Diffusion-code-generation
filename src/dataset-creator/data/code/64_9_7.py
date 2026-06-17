import datetime
from dateutil import parser as dt_parser
def format_datetime_localized(dt_instance: datetime.datetime) -> str:
    if not isinstance(dt_instance, (datetime.date, datetime.datetime)):
        raise TypeError("Input must be a datetime or date object.")
    return dt_instance.strftime("%B %d, %Y")
if __name__ == '__main__':
    utc_time = datetime.datetime(2023, 10, 5, 14, 30)
    local_time = datetime.datetime.now()
    print(f"UTC Time: {format_datetime_localized(utc_time)}")
    print(f"Local Time: {format_datetime_localized(local_time)}")