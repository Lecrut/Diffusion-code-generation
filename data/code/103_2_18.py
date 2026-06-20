import time

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

def get_elapsed_time_since_midnight():
    current_time = time.time()
    start_of_day = time.mktime(time.localtime())
    elapsed_seconds = int(current_time - start_of_day)
    hours, remainder = divmod(elapsed_seconds, SECONDS_PER_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_PER_MINUTE)
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    print(get_elapsed_time_since_midnight())