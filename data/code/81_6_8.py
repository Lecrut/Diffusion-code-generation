from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        times = [line.strip() for line in file.readlines()]
    
    time_format = "%H:%M:%S"
    start_time = datetime.strptime(times[0], time_format)
    end_time = datetime.strptime(times[1], time_format)
    
    elapsed_time = end_time - start_time
    return str(elapsed_time)

if __name__ == '__main__':
    sample_file_path = 'sample_times.txt'
    print(calculate_time_elapsed(sample_file_path))