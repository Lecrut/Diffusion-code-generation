from datetime import datetime

def time_elapsed(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    delta = end_time - start_time
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    start = "2023-10-01 12:00:00"
    end = "2023-10-01 14:30:00"
    print(time_elapsed(start, end))