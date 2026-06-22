import time

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def get_weekday_for_date(date_str):
    struct_time = time.strptime(date_str, "%Y-%m-%d")
    timestamp = time.mktime(struct_time)
    local_time = time.localtime(timestamp)
    weekday_code = local_time.tm_wday
    return WEEKDAY_MAP[weekday_code]

if __name__ == '__main__':
    target_date = '2023-01-01'
    weekday_name = get_weekday_for_date(target_date)
    print(weekday_name)