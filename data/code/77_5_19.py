def time_to_minutes(func):

    def wrapper(duration_str):
        parts = duration_str.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        total_minutes = hours * 60 + minutes + seconds / 60.0
        return func(total_minutes)
    return wrapper

@time_to_minutes
def process_time(minutes):
    return minutes * 2
if __name__ == '__main__':
    duration1 = '1:30:00'
    result1 = process_time(duration1)
    print(result1)
    duration2 = '0:05:45'
    result2 = process_time(duration2)
    print(result2)
    duration3 = '2:0:0'
    result3 = process_time(duration3)
    print(result3)