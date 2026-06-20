from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        time_points = [line.strip() for line in file.readlines()]
    
    start_time = datetime.strptime(time_points[0], '%H:%M:%S')
    end_time = datetime.strptime(time_points[1], '%H:%M:%S')
    
    elapsed_time = (end_time - start_time).total_seconds()
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"

if __name__ == '__main__':
    sample_file_path = 'sample_times.txt'
    print(calculate_time_elapsed(sample_file_path))