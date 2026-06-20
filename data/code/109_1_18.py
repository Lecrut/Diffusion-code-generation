def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def seconds_left_in_month(timestamp):
    import time
    current_time = time.localtime(timestamp)
    current_year = current_time.tm_year
    current_month = current_time.tm_mon
    
    if current_month == 12:
        next_month = (current_year + 1, 1)
    else:
        next_month = (current_year, current_month + 1)
    
    days_left_in_current_month = days_in_month(current_year, current_month) - current_time.tm_mday
    seconds_per_day = 24 * 60 * 60
    return days_left_in_current_month * seconds_per_day

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))