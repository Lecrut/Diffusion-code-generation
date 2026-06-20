from datetime import datetime

def time_elapsed_since_midnight():
    hardcoded_date = datetime(2023, 4, 1)
    current_time = datetime.now()
    start_of_day = datetime.combine(hardcoded_date, datetime.min.time())
    elapsed_time = current_time - start_of_day
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())