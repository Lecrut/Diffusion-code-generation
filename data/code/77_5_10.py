def time_to_minutes_decorator(func):

    def wrapper(duration_str):
        parts = duration_str.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid input format. Expected 'HH:MM:SS'")
        hours, minutes, seconds = map(int, parts)
        total_minutes = hours * 60 + minutes + seconds / 60
        return func(total_minutes)
    return wrapper

@time_to_minutes_decorator
def process_time(minutes):
    return minutes * 1.5
if __name__ == '__main__':
    duration1 = '1:30:00'
    result1 = process_time(duration1)
    print(result1)
    duration2 = '0:05:30'
    result2 = process_time(duration2)
    print(result2)
    duration3 = '2:15:45'
    result3 = process_time(duration3)
    print(result3)