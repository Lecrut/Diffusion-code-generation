import datetime

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_current_day_of_week():
    return days[datetime.datetime.now().weekday()]

if __name__ == '__main__':
    print(get_current_day_of_week())