import datetime

def calculate_elapsed_time():
    today = datetime.datetime(2023, 4, 1)
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(today, datetime.time.min)
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    elapsed_seconds = calculate_elapsed_time()
    print(f"Time elapsed since midnight: {elapsed_seconds} seconds")