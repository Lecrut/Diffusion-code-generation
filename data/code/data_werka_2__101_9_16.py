import datetime
import calendar

DATE_FORMAT = "%Y-%m-%d"
TARGET_DATE = "2023-11-11"

def determine_weekday(date_string: str) -> str:
    parsed_date = datetime.datetime.strptime(date_string, DATE_FORMAT)
    weekday_index = parsed_date.weekday()
    weekday_name = calendar.day_name[weekday_index]
    return weekday_name.upper()

if __name__ == '__main__':
    result = determine_weekday(TARGET_DATE)
    print(result)