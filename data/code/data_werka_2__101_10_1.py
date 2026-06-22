import calendar

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def calculate_day_of_week(year: int, month: int, day: int) -> str:
    weekday_index = calendar.weekday(year, month, day)
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    result = calculate_day_of_week(year, month, day)
    print(result)