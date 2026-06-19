from datetime import datetime

def calculate_net_time_difference(time_string, delimiter=';'):
    time_format = "%Y-%m-%d %H:%M:%S"
    times = [datetime.strptime(time_str.strip(), time_format) for time_str in time_string.split(delimiter)]
    earliest_time = min(times)
    latest_time = max(times)
    net_difference = latest_time - earliest_time
    return net_difference.total_seconds()

if __name__ == '__main__':
    sample_times = "2023-01-01 12:00:00; 2023-01-02 14:30:00; 2023-01-01 09:45:00"
    result = calculate_net_time_difference(sample_times)
    print(result)