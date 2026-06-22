import datetime

DAY_MAPPING = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_day_of_week():
    today = datetime.date.today()
    return DAY_MAPPING[today.weekday()]

if __name__ == '__main__':
    print(get_day_of_week())