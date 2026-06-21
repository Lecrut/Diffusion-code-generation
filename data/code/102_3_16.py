import time

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def check_weekday_status():
    current_time = time.localtime()
    weekday_index = current_time.tm_wday
    day_name = WEEKDAY_MAP.get(weekday_index, "Unknown")
    is_weekday = weekday_index < 5
    return {
        "is_weekday": is_weekday,
        "day_name": day_name,
        "weekday_index": weekday_index
    }

if __name__ == '__main__':
    result = check_weekday_status()
    print(result["is_weekday"])
    print(result["day_name"])
    print(result["weekday_index"])