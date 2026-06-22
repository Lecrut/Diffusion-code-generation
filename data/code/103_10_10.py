import datetime

def calculate_elapsed_time_since_start_of_day(target_date):
    start_of_day = datetime.datetime.combine(target_date, datetime.time.min)
    now = datetime.datetime.now()
    elapsed = now - start_of_day
    return elapsed

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    result = calculate_elapsed_time_since_start_of_day(sample_date)
    print(result)