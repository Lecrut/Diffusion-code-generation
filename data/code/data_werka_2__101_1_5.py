import calendar

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_weekday_name(year, month, day):
    index = calendar.weekday(year, month, day)
    return WEEKDAY_MAP[index]

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 5))