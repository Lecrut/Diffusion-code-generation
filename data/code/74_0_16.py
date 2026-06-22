import datetime
import calendar

DAY_MAPPING = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_current_weekday():
    today = datetime.date.today()
    weekday_index = today.weekday()
    return DAY_MAPPING[weekday_index]

if __name__ == '__main__':
    day_name = get_current_weekday()
    print(day_name)