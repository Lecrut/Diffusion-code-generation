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

def determine_weekday(date_string):
    parsed_date = datetime.date.fromisoformat(date_string)
    index = parsed_date.weekday()
    return WEEKDAY_MAP[index]

if __name__ == '__main__':
    target = '2024-07-04'
    weekday_name = determine_weekday(target)
    print(weekday_name)