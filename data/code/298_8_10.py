from datetime import datetime, timedelta

def time_difference(start_time, end_time):
    start_dt = datetime.strptime(start_time, '%H:%M')
    end_dt = datetime.strptime(end_time, '%H:%M')
    
    if end_dt < start_dt:
        end_dt += timedelta(days=1)
    
    diff = end_dt - start_dt
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(time_difference('22:00', '06:10'))