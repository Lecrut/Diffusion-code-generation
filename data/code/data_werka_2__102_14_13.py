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

def is_date_weekday(year, month, day):
    try:
        weekday_index = calendar.weekday(year, month, day)
        is_weekday = weekday_index < 5
        return is_weekday
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    test_dates = [
        (2023, 10, 23),
        (2023, 10, 28),
        (2023, 2, 29),
    ]
    for y, m, d in test_dates:
        try:
            result = is_date_weekday(y, m, d)
            print(result)
        except ValueError as e:
            print(str(e))