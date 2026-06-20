import time

def seconds_left_in_month(timestamp):
    current_time = time.localtime(timestamp)
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if current_year % 4 == 0 and current_year % 100 != 0 or current_year % 400 == 0:
        days_in_month[2] = 29
    last_day_of_current_month = days_in_month[current_month]
    seconds_until_end_of_month = (last_day_of_current_month - current_time.tm_mday) * 86400 + (23 - current_time.tm_hour) * 3600 + (59 - current_time.tm_min) * 60 + (60 - current_time.tm_sec)
    return seconds_until_end_of_month
if __name__ == '__main__':
    sample_timestamp = time.mktime((2023, 10, 15, 14, 30, 0, 0, 0, 0))
    print(seconds_left_in_month(sample_timestamp))