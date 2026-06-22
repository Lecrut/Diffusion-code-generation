import time

WEEKDAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def determine_weekday(date_string):
    parsed_time = time.strptime(date_string, "%Y-%m-%d")
    timestamp = time.mktime(parsed_time)
    local_time = time.localtime(timestamp)
    weekday_code = local_time.tm_wday
    return WEEKDAY_NAMES[weekday_code]

if __name__ == '__main__':
    target_date = '2023-01-01'
    computed_weekday = determine_weekday(target_date)
    print(computed_weekday)