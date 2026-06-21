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

def get_weekday_name(date_str):
    date_obj = datetime.date.fromisoformat(date_str)
    index = date_obj.weekday()
    return WEEKDAY_MAP[index]

if __name__ == '__main__':
    target = '2024-07-04'
    name = get_weekday_name(target)
    print(name)