from datetime import datetime

def milliseconds_elapsed_today() -> int:
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    return int(total_seconds * 1000)

if __name__ == '__main__':
    result = milliseconds_elapsed_today()
    print(result)