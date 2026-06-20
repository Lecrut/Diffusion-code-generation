from datetime import datetime

def time_difference_hours(time1_str, time2_str):
    time_format = '%H:%M:%S'
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)
    
    if time1 > time2:
        time2 += timedelta(days=1)
    
    difference = time2 - time1
    return difference.total_seconds() / 3600

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)