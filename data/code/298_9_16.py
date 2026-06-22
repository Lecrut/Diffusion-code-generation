from datetime import datetime

def time_difference(time1, time2):
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    
    if start_time > end_time:
        end_time += timedelta(days=1)
    
    delta = end_time - start_time
    return int(delta.total_seconds() / 60)

if __name__ == '__main__':
    print(time_difference('09:45', '23:15'))
    print(time_difference('23:15', '09:45'))