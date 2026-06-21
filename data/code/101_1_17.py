import calendar
import datetime

WEEKDAY_START = 0
WEEKDAY_END = 7
DATE_FORMAT = "%A"

def get_weekday_name(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        weekday_index = date_obj.weekday()
        if weekday_index < WEEKDAY_START or weekday_index >= WEEKDAY_END:
            raise ValueError(f"Invalid weekday index: {weekday_index}")
        return calendar.day_name[weekday_index]
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    result = get_weekday_name(sample_year, sample_month, sample_day)
    print(result)