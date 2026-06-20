import time

def calculate_milliseconds_today():
    current_time = time.time()
    start_of_day_timestamp = int(current_time // 86400) * 86400
    milliseconds_passed = (current_time - start_of_day_timestamp) * 1000
    return int(milliseconds_passed)

if __name__ == '__main__':
    milliseconds = calculate_milliseconds_today()
    print(milliseconds)