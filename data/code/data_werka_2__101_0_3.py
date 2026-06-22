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

def get_day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday_index = date_obj.weekday()
    return DAYS_MAPPING[weekday_index]

if __name__ == '__main__':
    target_date = "2023-10-05"
    day_name = get_day_of_week(target_date)
    print(day_name)