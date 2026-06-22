import datetime

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_current_day_of_week():
    today = datetime.date.today()
    weekday_index = today.weekday()
    if weekday_index not in WEEKDAY_MAP:
        raise ValueError(f"Invalid weekday index: {weekday_index}")
    return WEEKDAY_MAP[weekday_index]

if __name__ == '__main__':
    result = get_current_day_of_week()
    print(result)