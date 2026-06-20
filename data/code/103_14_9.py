import datetime

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60

def get_elapsed_time():
    start_time = datetime.datetime(2023, 4, 1, 9, 0, 0)
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    
    hours = elapsed_time.seconds // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)
    minutes = (elapsed_time.seconds // SECONDS_PER_MINUTE) % MINUTES_PER_HOUR
    seconds = elapsed_time.seconds % SECONDS_PER_MINUTE
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    print(get_elapsed_time())