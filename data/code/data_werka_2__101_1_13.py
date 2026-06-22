import calendar
import math

DAYS_IN_WEEK = 7
WEEKDAY_NAMES = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

def get_weekday_name(year, month, day):
    day_of_week = calendar.weekday(year, month, day)
    return WEEKDAY_NAMES[day_of_week % DAYS_IN_WEEK]

if __name__ == '__main__':
    TARGET_YEAR = 2024
    TARGET_MONTH = 1
    TARGET_DAY = 1
    computed_weekday = get_weekday_name(TARGET_YEAR, TARGET_MONTH, TARGET_DAY)
    print(computed_weekday)