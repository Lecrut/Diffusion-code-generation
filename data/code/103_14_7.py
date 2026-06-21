import time

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def format_elapsed_time(start_epoch, end_epoch):
    diff = end_epoch - start_epoch
    total_seconds = int(diff)
    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    result = format_elapsed_time(start_time, end_time)
    print(result)