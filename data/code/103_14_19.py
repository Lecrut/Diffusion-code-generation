import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def calculate_elapsed_time_from_start(start_time, current_time):
    delta = current_time - start_time
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_seconds = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    result = calculate_elapsed_time_from_start(start_of_day, now)
    print(result)