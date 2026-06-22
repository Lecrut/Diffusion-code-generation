import datetime

WEEKDAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DATE_FORMAT = "%Y-%m-%d"
TARGET_DATE = "2023-10-05"

def determine_weekday(date_string):
    parsed = datetime.datetime.strptime(date_string, DATE_FORMAT)
    weekday_index = parsed.weekday()
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    result = determine_weekday(TARGET_DATE)
    print(result)