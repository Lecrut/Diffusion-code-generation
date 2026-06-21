import datetime

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_january_1_day(year):
    target_date = datetime.date(year, 1, 1)
    weekday_index = target_date.weekday()
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    year = 2024
    day_name = get_january_1_day(year)
    print(day_name)