import time

def get_weekday(date_str):
    timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d"))
    weekday_tuple = time.localtime(timestamp)
    return weekday_tuple.tm_wday

if __name__ == '__main__':
    date_str = '2023-01-01'
    result = get_weekday(date_str)
    print(result)