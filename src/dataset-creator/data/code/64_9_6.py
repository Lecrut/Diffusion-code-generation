import datetime
from dateutil import parser as dt_parser
def convert_datetime_to_localized_string(dt_instance: datetime.datetime) -> str:
    if not isinstance(dt_instance, datetime.datetime):
        raise TypeError("Input must be a datetime object")
    return dt_instance.strftime("%B %d, %Y at %I:%M%p")
if __name__ == '__main__':
    utc_time = datetime.datetime(2023, 10, 5, 14, 30)
    local_time = datetime.datetime.now()
    print(f"UTC: {convert_datetime_to_localized_string(utc_time)}")
    print(f"Local: {convert_datetime_to_localized_string(local_time)}")