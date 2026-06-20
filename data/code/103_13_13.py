import time

def calculate_fractional_day():
    current_time = time.localtime()
    elapsed_seconds_today = (current_time.tm_hour * 3600) + (current_time.tm_min * 60) + current_time.tm_sec
    total_seconds_in_a_day = 24 * 3600
    fractional_part = elapsed_seconds_today / total_seconds_in_a_day
    return fractional_part

if __name__ == '__main__':
    print(calculate_fractional_day())