import datetime

DAY_NAMES = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

JANUARY_1_YEAR = 2024
JANUARY_1_MONTH = 1
JANUARY_1_DAY = 1

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    index = date_obj.weekday()
    return DAY_NAMES[index]

if __name__ == '__main__':
    result = get_day_of_week(JANUARY_1_YEAR, JANUARY_1_MONTH, JANUARY_1_DAY)
    print(result)