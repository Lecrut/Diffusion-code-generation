from datetime import datetime

def calculate_time_difference(file_path):
    with open(file_path, 'r') as file:
        times = [line.strip() for line in file.readlines()]
    
    time_format = "%H:%M:%S"
    start_time = datetime.strptime(times[0], time_format)
    end_time = datetime.strptime(times[1], time_format)
    
    time_difference = end_time - start_time
    return str(time_difference)

if __name__ == '__main__':
    print(calculate_time_difference('times.txt'))