from datetime import datetime, timedelta

def calculate_time_difference(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    time_difference = end_time - start_time
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60
    
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    print(calculate_time_difference('22:00', '06:10'))