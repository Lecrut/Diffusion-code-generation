import datetime

DAY_MAPPING = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def determine_weekday(year, month, day):
    target_date = datetime.date(year, month, day)
    weekday_index = target_date.weekday()
    return DAY_MAPPING[weekday_index]

if __name__ == '__main__':
    print(determine_weekday(2024, 2, 29))