from datetime import datetime

def calculate_duration(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    duration = (end_time - start_time).seconds
    return duration

if __name__ == '__main__':
    total_duration = calculate_duration('11:30', '14:15')
    print(total_duration)