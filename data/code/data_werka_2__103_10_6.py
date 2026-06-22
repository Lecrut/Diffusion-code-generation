import datetime

def calculate_elapsed_time_since_start_of_day():
    today = datetime.date(2023, 10, 5)
    start_of_day = datetime.datetime.combine(today, datetime.time.min)
    now = datetime.datetime.now()
    elapsed = now - start_of_day
    return elapsed.total_seconds()

if __name__ == '__main__':
    result = calculate_elapsed_time_since_start_of_day()
    print(result)