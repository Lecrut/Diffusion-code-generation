from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        start_time_str = file.readline().strip()
        end_time_str = file.readline().strip()

    start_time = datetime.strptime(start_time_str, '%H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%H:%M:%S')

    time_difference = (end_time - start_time).total_seconds()
    hours, remainder = divmod(time_difference, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == '__main__':
    sample_file_path = 'times.txt'
    print(calculate_time_elapsed(sample_file_path))