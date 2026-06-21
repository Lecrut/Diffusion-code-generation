import datetime

def format_elapsed_time(start_time, end_time):
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    result = format_elapsed_time(start_of_day, now)
    print(result)