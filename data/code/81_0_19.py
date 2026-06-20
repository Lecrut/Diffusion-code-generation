from datetime import datetime

def calculate_time_elapsed(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    if end < start:
        end += timedelta(days=1)
    time_difference = end - start
    return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    start = "23:59"
    end = "00:01"
    print(calculate_time_elapsed(start, end))