import calendar

def get_weekday_name(year, month, day):
    weekday_index = calendar.weekday(year, month, day)
    weekday_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    return weekday_names[weekday_index]

if __name__ == '__main__':
    result = get_weekday_name(2023, 10, 5)
    print(result)