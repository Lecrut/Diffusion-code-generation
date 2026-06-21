from datetime import datetime

def calculate_net_time_difference(time_string):
    times = time_string.split(';')
    if not times:
        raise ValueError('Input string is empty or does not contain any time points.')
    try:
        parsed_times = [datetime.strptime(time.strip(), '%Y-%m-%d %H:%M:%S') for time in times]
    except ValueError as e:
        raise ValueError(f'Invalid time format: {e}')
    earliest_time = min(parsed_times)
    latest_time = max(parsed_times)
    net_difference = latest_time - earliest_time
    return net_difference
if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00; 2023-01-02 15:30:00; 2023-01-01 09:45:00'
    net_difference = calculate_net_time_difference(sample_input)
    print(net_difference)