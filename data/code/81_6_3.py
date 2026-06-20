from datetime import datetime

def calculate_time_elapsed(file_path):
    with open(file_path, 'r') as file:
        times = [line.strip() for line in file.readlines()]
        start_time = datetime.strptime(times[0], '%H:%M')
        end_time = datetime.strptime(times[1], '%H:%M')
        time_difference = end_time - start_time
        return str(time_difference)

if __name__ == '__main__':
    print(calculate_time_elapsed('times.txt'))