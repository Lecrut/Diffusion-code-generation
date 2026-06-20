import datetime

def calculate_elapsed_time():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed_time = now - start_of_day
    return elapsed_time

if __name__ == '__main__':
    elapsed_time = calculate_elapsed_time()
    print(f"Time elapsed since midnight: {elapsed_time}")