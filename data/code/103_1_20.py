import datetime

def get_milliseconds_elapsed_today() -> int:
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    milliseconds = int(total_seconds * 1000)
    return milliseconds

if __name__ == '__main__':
    result = get_milliseconds_elapsed_today()
    print(result)