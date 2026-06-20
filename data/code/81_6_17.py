from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_time_str = lines[0].strip()
        end_time_str = lines[1].strip()

    start_time = datetime.strptime(start_time_str, '%H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%H:%M:%S')

    time_difference = end_time - start_time
    total_seconds = time_difference.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(calculate_time_elapsed('time_points.txt'))