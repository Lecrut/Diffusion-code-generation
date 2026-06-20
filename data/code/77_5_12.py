def time_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in 'hours:minutes:seconds' format")
    hours, minutes, seconds = map(int, parts)
    return hours * 60 + minutes + seconds / 60

def time_decorator(func):

    def wrapper(time_str):
        if not isinstance(time_str, str) or ':' not in time_str:
            raise ValueError('Input must be a string representing time')
        return func(time_to_minutes(time_str))
    return wrapper

@time_decorator
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