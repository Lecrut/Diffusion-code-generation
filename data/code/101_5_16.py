import time

def get_weekday(date_str):
    timestamp = time.mktime(time.strptime(date_str, '%Y-%m-%d'))
    weekday = time.localtime(timestamp).tm_wday
    return weekday

if __name__ == '__main__':
    sample_date = '2023-01-01'
    print(get_weekday(sample_date))