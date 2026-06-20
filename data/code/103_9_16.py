import datetime

def calculate_elapsed_time():
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    start_of_day_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = now_utc - start_of_day_utc
    return elapsed_time

if __name__ == '__main__':
    elapsed_time = calculate_elapsed_time()
    hours = elapsed_time.seconds // 3600
    minutes = (elapsed_time.seconds // 60) % 60
    seconds = elapsed_time.seconds % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")