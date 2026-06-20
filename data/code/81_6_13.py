from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        time_points = [line.strip() for line in file.readlines()]
    
    start_time = datetime.strptime(time_points[0], '%H:%M')
    end_time = datetime.strptime(time_points[1], '%H:%M')
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    time_difference = end_time - start_time
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    return f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}"

if __name__ == '__main__':
    print(calculate_time_elapsed('time_points.txt'))