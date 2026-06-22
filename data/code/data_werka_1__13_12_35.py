from datetime import datetime

def calculate_net_time_difference(time_string):
    time_points = time_string.split(';')
    times = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in time_points]
    earliest_time = min(times)
    latest_time = max(times)
    net_difference = latest_time - earliest_time
    return net_difference
if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00;2023-01-01 14:30:00;2023-01-01 13:45:00'
    result = calculate_net_time_difference(sample_input)
    print(result)