import datetime

WEEKDAY_NAMES = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

DATE_FORMAT = "%Y-%m-%d"

def determine_weekday(date_string: str) -> str:
    parsed = datetime.datetime.strptime(date_string, DATE_FORMAT)
    weekday_index = parsed.weekday()
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    target = "2023-10-05"
    day = determine_weekday(target)
    print(day)