from datetime import datetime

def calculate_time_difference(file_path):
    with open(file_path, 'r') as file:
        time_points = [line.strip() for line in file.readlines()]
    
    if len(time_points) != 2:
        raise ValueError("File must contain exactly two time points.")
    
    start_time = datetime.strptime(time_points[0], "%H:%M")
    end_time = datetime.strptime(time_points[1], "%H:%M")
    
    time_difference = (end_time - start_time).total_seconds() / 3600
    
    hours, remainder = divmod(time_difference, 1)
    minutes = int(remainder * 60)
    
    return f"{int(hours)} hour{'s' if hours != 1 else ''} and {minutes} minute{'s' if minutes != 1 else ''}"

if __name__ == '__main__':
    print(calculate_time_difference('time_points.txt'))