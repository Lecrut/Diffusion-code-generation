import calendar

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def determine_weekday(year: int, month: int, day: int) -> str:
    index = calendar.weekday(year, month, day)
    return WEEKDAY_NAMES[index]

if __name__ == '__main__':
    result = determine_weekday(2023, 12, 25)
    print(result)