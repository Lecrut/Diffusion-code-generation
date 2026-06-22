import datetime

def calculate_time_elapsed_since_midnight():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed = now - start_of_day
    return elapsed

if __name__ == '__main__':
    result = calculate_time_elapsed_since_midnight()
    print(result)