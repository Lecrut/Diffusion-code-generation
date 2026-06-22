import datetime

def calculate_elapsed_time_since_start_of_day():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
    elapsed = now - start_of_day
    return elapsed

if __name__ == '__main__':
    result = calculate_elapsed_time_since_start_of_day()
    print(result)