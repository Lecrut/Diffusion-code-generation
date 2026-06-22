import datetime

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_current_day_name():
    today = datetime.date.today()
    weekday_index = today.weekday()
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    result = get_current_day_name()
    print(result)