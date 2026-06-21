from datetime import datetime

def parse_time_string(time_string, delimiter=';'):
    time_parts = time_string.split(delimiter)
    times = [datetime.strptime(t.strip(), '%Y-%m-%d %H:%M:%S') for t in time_parts]
    return times

def calculate_earliest_and_latest(times):
    earliest_time = min(times)
    latest_time = max(times)
    return earliest_time, latest_time

def compute_net_difference(earliest_time, latest_time):
    net_difference = latest_time - earliest_time
    return net_difference

def calculate_net_time_difference(time_string, delimiter=';'):
    times = parse_time_string(time_string, delimiter)
    earliest_time, latest_time = calculate_earliest_and_latest(times)
    net_difference = compute_net_difference(earliest_time, latest_time)
    return net_difference

if __name__ == '__main__':
    sample_input = '2023-01-05 08:00:00;2023-01-07 16:45:00;2023-01-06 11:30:00'
    result = calculate_net_time_difference(sample_input)
    print(result)