from datetime import datetime

def time_elapsed(start_time: str, end_time: str) -> float:
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    if end < start:
        end += timedelta(days=1)
    return (end - start).total_seconds() / 3600

if __name__ == '__main__':
    print(time_elapsed("23:59", "00:01"))