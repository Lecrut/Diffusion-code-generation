from datetime import datetime

def time_elapsed_in_hours(start_time, end_time):
    start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    time_difference = end_dt - start_dt
    return time_difference.total_seconds() / 3600

if __name__ == '__main__':
    sample_start_time = "2023-10-01 14:00:00"
    sample_end_time = "2023-10-05 18:30:00"
    print(time_elapsed_in_hours(sample_start_time, sample_end_time))