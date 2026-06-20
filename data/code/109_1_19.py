import time

def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def seconds_left_in_month(timestamp):
    current_time = time.localtime(timestamp)
    current_year, current_month, _, _, _, _ = current_time
    last_day_of_current_month = days_in_month(current_year, current_month)
    seconds_until_end_of_month = (last_day_of_current_month - current_time.tm_mday) * 86400 + (23 - current_time.tm_hour) * 3600 + (59 - current_time.tm_min) * 60 + (60 - current_time.tm_sec)
    return seconds_until_end_of_month

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))