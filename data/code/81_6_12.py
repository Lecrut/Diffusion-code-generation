from datetime import datetime

def calculate_time_difference(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_time_str = lines[0].strip()
        end_time_str = lines[1].strip()

        start_time = datetime.strptime(start_time_str, '%H:%M:%S')
        end_time = datetime.strptime(end_time_str, '%H:%M:%S')

        if end_time < start_time:
            end_time += timedelta(days=1)

        time_difference = end_time - start_time
        return str(time_difference).split('.')[0]

if __name__ == '__main__':
    sample_file_path = 'sample_times.txt'
    result = calculate_time_difference(sample_file_path)
    print(result)