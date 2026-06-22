from datetime import datetime, timedelta

def time_difference(time1, time2):
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    diff = end_time - start_time
    hours = diff.seconds // 3600
    minutes = (diff.seconds // 60) % 60
    seconds = diff.seconds % 60
    
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(time_difference('22:00', '06:10'))