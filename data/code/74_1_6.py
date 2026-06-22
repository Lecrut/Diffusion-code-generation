import datetime

DAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_current_day():
    today = datetime.date.today()
    return DAY_MAP[today.weekday()]

if __name__ == '__main__':
    result = get_current_day()
    print(result)