import time

def get_weekday_from_timestamp(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) != 10:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    try:
        struct_time = time.strptime(date_str, "%Y-%m-%d")
        timestamp = time.mktime(struct_time)
        local_time = time.localtime(timestamp)
        weekday_index = local_time.tm_wday
        weekday_map = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        return weekday_map[weekday_index]
    except ValueError as e:
        raise ValueError(f"Invalid date: {date_str}") from e

if __name__ == '__main__':
    target_date = '2023-01-01'
    result = get_weekday_from_timestamp(target_date)
    print(result)