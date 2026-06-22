from datetime import datetime

def calculate_net_time_difference(time_string, delimiter=';'):
    times = [datetime.strptime(t.strip(), '%Y-%m-%d %H:%M:%S') for t in time_string.split(delimiter)]
    if not times:
        raise ValueError("No valid times found in the input string.")
    
    earliest_time = min(times)
    latest_time = max(times)
    net_difference = latest_time - earliest_time
    return net_difference

if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00;2023-01-03 08:15:00;2023-01-01 10:45:00'
    result = calculate_net_time_difference(sample_input)
    print(result.total_seconds())