import datetime

def calculate_duration(time_str1, time_str2):
    format = '%H:%M'
    time1 = datetime.datetime.strptime(time_str1, format)
    time2 = datetime.datetime.strptime(time_str2, format)
    
    if time2 >= time1:
        duration_seconds = (time2 - time1).seconds
    else:
        duration_seconds = ((datetime.datetime.combine(datetime.date.today(), time2.time()) + 
                             datetime.timedelta(days=1)) - 
                            datetime.datetime.combine(datetime.date.today(), time1.time())).seconds
    
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return hours, minutes, seconds

if __name__ == '__main__':
    time_a = "22:00"
    time_b = "06:10"
    result_hours, result_minutes, result_seconds = calculate_duration(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {result_hours} hours, {result_minutes} minutes, {result_seconds} seconds")