import datetime

def time_elapsed_since_midnight():
    hardcoded_date = datetime.date(2023, 4, 1)
    current_time = datetime.datetime.now()
    midnight = datetime.datetime.combine(hardcoded_date, datetime.time.min)
    elapsed_time = current_time - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    elapsed_seconds = time_elapsed_since_midnight()
    print(f"Time elapsed since midnight: {elapsed_seconds} seconds")