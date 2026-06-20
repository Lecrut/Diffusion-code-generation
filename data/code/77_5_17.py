import re
CONVERSION_MINUTES_PER_HOUR = 60
CONVERSION_SECONDS_PER_MINUTE = 60

def time_to_minutes(time_str):
    match = re.match('^(\\d+):(\\d+):(\\d+)$', time_str)
    if not match:
        raise ValueError('Invalid time format')
    hours, minutes, seconds = map(int, match.groups())
    return hours * CONVERSION_MINUTES_PER_HOUR + minutes + seconds / CONVERSION_SECONDS_PER_MINUTE

def convert_duration_to_minutes(func):

    def wrapper(duration_str):
        total_minutes = time_to_minutes(duration_str)
        return func(total_minutes)
    return wrapper

@convert_duration_to_minutes
def process_time(minutes):
    return minutes * 2
if __name__ == '__main__':
    duration1 = '1:30:00'
    result1 = process_time(duration1)
    print(result1)
    duration2 = '0:05:45'
    result2 = process_time(duration2)
    print(result2)
    duration3 = '2:15:45'
    result3 = process_time(duration3)
    print(result3)