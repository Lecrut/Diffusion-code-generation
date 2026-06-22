from datetime import datetime

TIME_FORMAT = "%H:%M"
SECONDS_PER_HOUR = 3600

def time_difference(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, TIME_FORMAT)
    end_time = datetime.strptime(end_time_str, TIME_FORMAT)
    duration = (end_time - start_time).seconds
    return duration

if __name__ == '__main__':
    total_seconds = time_difference('11:30', '14:15')
    print(total_seconds)