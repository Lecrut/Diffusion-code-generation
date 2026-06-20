import time

def is_valid_time(time_value):
    return isinstance(time_value, time.struct_time) and len(time_value) == 9

def calculate_elapsed_seconds_since_midnight():
    if not is_valid_time(time.localtime()):
        raise ValueError("Invalid time value")
    
    now = time.time()
    midnight = time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, 0, 0, 0, 0, 0, -1))
    elapsed_seconds = int(now - midnight)
    return elapsed_seconds

if __name__ == '__main__':
    elapsed = calculate_elapsed_seconds_since_midnight()
    print(elapsed)