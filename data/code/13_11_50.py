from datetime import datetime

def parse_time_string(time_string, delimiter=';'):
    return [datetime.strptime(t.strip(), '%Y-%m-%d %H:%M:%S') for t in time_string.split(delimiter)]

def find_earliest_and_latest(times):
    return min(times), max(times)

def compute_net_difference(earliest_time, latest_time):
    return (latest_time - earliest_time).total_seconds()

def calculate_net_time_difference(time_string, delimiter=';'):
    times = parse_time_string(time_string, delimiter)
    if not times:
        raise ValueError("No valid times found in the input string.")
    earliest_time, latest_time = find_earliest_and_latest(times)
    return compute_net_difference(earliest_time, latest_time)

if __name__ == '__main__':
    sample_input = '2023-01-05 08:00:00;2023-01-07 16:45:00;2023-01-06 13:30:00'
    result = calculate_net_time_difference(sample_input)
    print(result)