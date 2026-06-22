import time

def get_weekday_from_timestamp(date_str):
    timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d"))
    weekday_index = time.localtime(timestamp).tm_wday
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[weekday_index]

if __name__ == '__main__':
    date_str = '2023-01-01'
    result = get_weekday_from_timestamp(date_str)
    print(result)