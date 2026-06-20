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
def process_duration(minutes):
    return f"Processed duration: {minutes} minutes"

if __name__ == '__main__':
    result1 = process_duration('1:30:00')
    print(result1)
    result2 = process_duration('0:05:45')
    print(result2)
    result3 = process_duration('2:15:30')
    print(result3)