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

def find_weekday(date_str):
    struct_time = time.strptime(date_str, "%Y-%m-%d")
    timestamp = time.mktime(struct_time)
    local_time = time.localtime(timestamp)
    code = local_time.tm_wday
    return WEEKDAY_MAP[code]

if __name__ == '__main__':
    target = '2023-01-01'
    answer = find_weekday(target)
    print(answer)