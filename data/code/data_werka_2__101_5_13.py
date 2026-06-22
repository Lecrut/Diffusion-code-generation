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

DATE_FORMAT = "%Y-%m-%d"

def get_weekday_from_date(date_str):
    struct_time = time.strptime(date_str, DATE_FORMAT)
    timestamp = time.mktime(struct_time)
    local_time = time.localtime(timestamp)
    return WEEKDAY_MAP[local_time.tm_wday]

if __name__ == '__main__':
    target_date = '2023-01-01'
    weekday = get_weekday_from_date(target_date)
    print(weekday)