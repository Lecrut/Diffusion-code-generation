from datetime import datetime

def time_elapsed_in_hours(start_time, end_time):
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 9, 0)
    end = datetime(2023, 1, 1, 17, 30)
    result = time_elapsed_in_hours(start, end)
    print(result)