from datetime import datetime

def calculate_net_time_difference(time_string, delimiter=';'):
    time_parts = time_string.split(delimiter)
    times = [datetime.strptime(time.strip(), '%Y-%m-%d %H:%M:%S') for time in time_parts]
    earliest_time = min(times)
    latest_time = max(times)
    net_difference = latest_time - earliest_time
    return net_difference
if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00;2023-01-02 14:30:00;2023-01-01 10:45:00'
    result = calculate_net_time_difference(sample_input)
    print(result)