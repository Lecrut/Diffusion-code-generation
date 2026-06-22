import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_elapsed_time_string(reference_time):
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_PER_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_PER_MINUTE)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    now = datetime.datetime.now()
    result = get_elapsed_time_string(now)
    print(result)