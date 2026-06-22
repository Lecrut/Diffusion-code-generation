from datetime import datetime

def calculate_net_time_difference(time_string):
    time_format = "%Y-%m-%d %H:%M:%S"
    times = time_string.split(';')
    earliest_time = min(datetime.strptime(t, time_format) for t in times)
    latest_time = max(datetime.strptime(t, time_format) for t in times)
    net_difference = latest_time - earliest_time
    return net_difference.total_seconds()

if __name__ == '__main__':
    sample_times = "2023-01-01 12:00:00;2023-01-01 14:30:00;2023-01-01 13:45:00"
    net_difference = calculate_net_time_difference(sample_times)
    print(net_difference)