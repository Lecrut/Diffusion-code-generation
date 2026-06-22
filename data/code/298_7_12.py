import datetime

TIME_FORMAT = "%H:%M"
SECONDS_PER_MINUTE = 60

def calculate_duration(start_time_str, end_time_str):
    start_time = datetime.datetime.strptime(start_time_str, TIME_FORMAT)
    end_time = datetime.datetime.strptime(end_time_str, TIME_FORMAT)
    duration = (end_time - start_time).seconds
    return duration

if __name__ == '__main__':
    result = calculate_duration('11:30', '14:15')
    print(f"Total time duration: {result} seconds")