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

def determine_weekday(year, month, day):
    date_instance = datetime.date(year, month, day)
    weekday_index = date_instance.weekday()
    return DAY_MAP[weekday_index]

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_day = determine_weekday(target_year, target_month, target_day)
    print(computed_day)