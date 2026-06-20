import calendar

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_weekday_name(year, month, day):
    return DAY_NAMES[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    print(get_weekday_name(2023, 10, 26))
    print(get_weekday_name(2024, 1, 1))
    print(get_weekday_name(2025, 12, 31))