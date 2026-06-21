import time

def get_weekday_from_timestamp(date_string):
    timestamp = time.mktime(time.strptime(date_string, "%Y-%m-%d"))
    weekday_tuple = time.localtime(timestamp)
    weekday_name = time.strftime("%A", weekday_tuple)
    return weekday_name

if __name__ == '__main__':
    date_str = '2023-01-01'
    result = get_weekday_from_timestamp(date_str)
    print(result)