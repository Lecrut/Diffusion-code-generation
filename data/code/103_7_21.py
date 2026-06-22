import datetime

def calculate_time_elapsed_since_start_of_day():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.datetime.min.time())
    elapsed = now - start_of_day
    total_seconds = int(elapsed.total_seconds())
    return total_seconds

if __name__ == '__main__':
    result = calculate_time_elapsed_since_start_of_day()
    print(result)