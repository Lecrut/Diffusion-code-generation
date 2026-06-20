from datetime import datetime

def time_elapsed_in_hours(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    delta = end - start
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    print(time_elapsed_in_hours("2023-10-01 12:00:00", "2023-10-02 14:30:00"))