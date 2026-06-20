from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        start_time_str = file.readline().strip()
        end_time_str = file.readline().strip()

    start_time = datetime.strptime(start_time_str, '%H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%H:%M:%S')

    time_difference = end_time - start_time
    total_seconds = time_difference.total_seconds()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    sample_file_path = 'sample_times.txt'
    print(calculate_time_elapsed(sample_file_path))