import datetime

def calculate_time_elapsed():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.time.min)
    time_elapsed = now - start_of_day
    return time_elapsed.total_seconds()

if __name__ == '__main__':
    elapsed_time = calculate_time_elapsed()
    print(f"Time elapsed since the beginning of the day: {elapsed_time} seconds")