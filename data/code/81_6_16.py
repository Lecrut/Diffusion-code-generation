from datetime import datetime

def parse_time(time_str):
    return datetime.strptime(time_str.strip(), '%H:%M')

def calculate_time_difference(file_path):
    with open(file_path, 'r') as file:
        times = [parse_time(line) for line in file.readlines()]
        if len(times) != 2:
            raise ValueError("File must contain exactly two time points.")
        start_time, end_time = times
        return end_time - start_time

def format_duration(duration):
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == '__main__':
    file_path = 'times.txt'
    duration = calculate_time_difference(file_path)
    print(f"Total time elapsed: {format_duration(duration)}")