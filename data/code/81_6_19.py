from datetime import datetime

def parse_time(time_str):
    try:
        return datetime.strptime(time_str.strip(), '%H:%M')
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM.")

def calculate_elapsed_time(file_path):
    with open(file_path, 'r') as file:
        times = [line.strip() for line in file.readlines()]
        if len(times) != 2:
            raise ValueError("File must contain exactly two time points.")
        start_time = parse_time(times[0])
        end_time = parse_time(times[1])
        elapsed_time = end_time - start_time
        return elapsed_time

if __name__ == '__main__':
    result = calculate_elapsed_time('times.txt')
    print(f"Elapsed time: {result}")