import datetime

def time_difference(start_time_str, end_time_str):
    start_time = datetime.datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.datetime.strptime(end_time_str, '%H:%M')
    
    if end_time < start_time:
        end_time += datetime.timedelta(days=1)
    
    delta = end_time - start_time
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(time_difference('22:00', '06:10'))