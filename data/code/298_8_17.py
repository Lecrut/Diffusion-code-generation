import datetime

def calculate_duration(time_str1, time_str2):
    format = '%H:%M'
    time1 = datetime.datetime.strptime(time_str1, format)
    time2 = datetime.datetime.strptime(time_str2, format)
    
    if time2 >= time1:
        duration = time2 - time1
    else:
        duration = (time2 + datetime.timedelta(days=1)) - time1
    
    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    seconds = duration.seconds % 60
    
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    time_a = "22:00"
    time_b = "06:10"
    result = calculate_duration(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {result}")