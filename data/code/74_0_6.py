import datetime

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    weekday_number = current_date.weekday()
    return WEEKDAY_NAMES[weekday_number]

if __name__ == '__main__':
    print(get_current_day_of_week())