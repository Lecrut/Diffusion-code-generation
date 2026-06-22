from dateutil.parser import parse

DAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_day_of_week(date_string: str) -> str:
    parsed_date = parse(date_string)
    weekday_index = parsed_date.weekday()
    return DAY_MAP[weekday_index]

if __name__ == '__main__':
    target_date = 'January 15, 2023'
    day_name = get_day_of_week(target_date)
    print(day_name)