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

def get_weekday_name(date_tuple):
    year, month, day = date_tuple
    weekday_index = calendar.weekday(year, month, day)
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    sample_date = (2023, 10, 25)
    result = get_weekday_name(sample_date)
    print(result)