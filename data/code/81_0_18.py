from datetime import datetime

def time_elapsed(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    elapsed_time = end_time - start_time
    return elapsed_time.total_seconds() / 3600

if __name__ == '__main__':
    start_time = "2023-10-01 12:00:00"
    end_time = "2023-10-01 14:30:00"
    print(time_elapsed(start_time, end_time))