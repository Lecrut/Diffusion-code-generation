from datetime import datetime

def calculate_net_time_difference(time_string, delimiter=';'):
    time_format = "%Y-%m-%d %H:%M:%S"
    times = [datetime.strptime(t.strip(), time_format) for t in time_string.split(delimiter)]
    min_time = min(times)
    max_time = max(times)
    net_difference = max_time - min_time
    return net_difference

if __name__ == '__main__':
    sample_times = "2023-01-01 12:00:00; 2023-01-01 14:30:00; 2023-01-01 09:15:00"
    result = calculate_net_time_difference(sample_times)
    print(result)