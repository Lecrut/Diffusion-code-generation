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

def get_day_of_week(year, month, day):
    date_instance = datetime.date(year, month, day)
    index = date_instance.weekday()
    return DAY_MAP[index]

if __name__ == '__main__':
    result = get_day_of_week(2024, 2, 29)
    print(result)