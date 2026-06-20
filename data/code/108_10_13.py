import datetime

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_day_of_week(year, month, day):
    date_obj = datetime.datetime(year, month, day)
    return days_of_week[date_obj.weekday()]

if __name__ == '__main__':
    print(get_day_of_week(2024, 1, 1))