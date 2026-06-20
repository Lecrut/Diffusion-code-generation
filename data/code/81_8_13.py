from datetime import datetime, timedelta

def calculate_elapsed_time(start_time, end_time):
    elapsed_time = end_time - start_time
    return elapsed_time.total_seconds() / 3600
if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 9, 0)
    end_time = datetime(2023, 10, 1, 17, 30)
    print(calculate_elapsed_time(start_time, end_time))