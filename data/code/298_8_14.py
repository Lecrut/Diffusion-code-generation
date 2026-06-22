from datetime import datetime, timedelta

def calculate_time_difference(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    time_diff = end_time - start_time
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    seconds = time_diff.seconds % 60
    
    return hours, minutes, seconds

if __name__ == '__main__':
    start_time = '22:00'
    end_time = '06:10'
    hours, minutes, seconds = calculate_time_difference(start_time, end_time)
    print(f'Time difference: {hours} hours, {minutes} minutes, {seconds} seconds')