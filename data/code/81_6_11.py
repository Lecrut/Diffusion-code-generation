from datetime import datetime

def calculate_time_difference(file_path):
    with open(file_path, 'r') as file:
        times = [line.strip() for line in file.readlines()]
        start_time = datetime.strptime(times[0], '%H:%M')
        end_time = datetime.strptime(times[1], '%H:%M')
        time_difference = (end_time - start_time).seconds
        hours, remainder = divmod(time_difference, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(calculate_time_difference('times.txt'))