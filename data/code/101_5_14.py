import time

def compute_weekday_from_timestamp(date_str):
    parsed_tuple = time.strptime(date_str, "%Y-%m-%d")
    seconds_since_epoch = time.mktime(parsed_tuple)
    time_struct = time.localtime(seconds_since_epoch)
    day_index = time_struct.tm_wday
    mapping = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return mapping[day_index]

if __name__ == '__main__':
    input_date = '2023-01-01'
    day_name = compute_weekday_from_timestamp(input_date)
    print(day_name)