from datetime import datetime
from datetime import date

WEEKDAYS_COUNT = 5
ISO_FORMAT = "%Y-%m-%d"
SATURDAY_INDEX = 5
SUNDAY_INDEX = 6

def is_weekday(date_string: str) -> bool:
    parsed_date = datetime.strptime(date_string, ISO_FORMAT).date()
    weekday_index = parsed_date.weekday()
    is_weekday_flag = weekday_index < WEEKDAYS_COUNT
    return is_weekday_flag

if __name__ == '__main__':
    sample_dates = ["2023-10-06", "2023-10-07", "2023-10-08"]
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)