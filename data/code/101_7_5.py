import datetime

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def compute_weekday(date_str):
    date_obj = datetime.date.fromisoformat(date_str)
    index = date_obj.weekday()
    return WEEKDAY_NAMES[index]

if __name__ == '__main__':
    target_date = '2024-07-04'
    weekday_name = compute_weekday(target_date)
    print(weekday_name)