import datetime

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_weekday_name(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    return WEEKDAY_MAP[date_obj.weekday()]

if __name__ == '__main__':
    target_date = "2023-12-25"
    result = get_weekday_name(target_date)
    print(result)