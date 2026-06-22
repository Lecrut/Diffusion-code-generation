import datetime

def parse_time(time_str):
    return datetime.datetime.strptime(time_str, '%H:%M')

def calculate_duration(time_str1, time_str2):
    time1 = parse_time(time_str1)
    time2 = parse_time(time_str2)
    
    if time2 >= time1:
        duration = time2 - time1
    else:
        duration = (time2 + datetime.timedelta(days=1)) - time1
    
    return duration

def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    time_a = "22:00"
    time_b = "06:10"
    duration = calculate_duration(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {format_duration(duration)}")