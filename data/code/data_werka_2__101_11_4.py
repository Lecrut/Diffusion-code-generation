import datetime

DAYS_MAPPING = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    weekday_index = date_obj.weekday()
    return DAYS_MAPPING[weekday_index]

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)