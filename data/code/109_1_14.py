import time

def is_valid_timestamp(timestamp):
    try:
        time.localtime(timestamp)
        return True
    except ValueError:
        return False

def get_last_day_of_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    _, last_day = time.monthrange(year, month)
    return year, month, last_day

def seconds_left_in_month(timestamp):
    if not is_valid_timestamp(timestamp):
        raise ValueError("Invalid timestamp")
    
    dt_struct = time.localtime(timestamp)
    current_year, current_month, current_day = dt_struct.tm_year, dt_struct.tm_mon, dt_struct.tm_mday
    
    year, month, last_day = get_last_day_of_month(current_year, current_month)
    last_second_of_month = time.mktime((year, month, last_day, 23, 59, 59, 0, 0, 0))
    
    return int(last_second_of_month - timestamp)

if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))