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
def print_duration_in_minutes(minutes):
    print(f"Duration in minutes: {minutes:.2f}")

if __name__ == '__main__':
    duration1 = '1:30:00'
    result1 = print_duration_in_minutes(duration1)
    
    duration2 = '0:05:45'
    result2 = print_duration_in_minutes(duration2)
    
    duration3 = '2:15:30'
    result3 = print_duration_in_minutes(duration3)