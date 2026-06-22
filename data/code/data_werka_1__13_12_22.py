from datetime import datetime

def calculate_net_time_difference(time_string):
    times = time_string.split(';')
    earliest_time = min(times, key=lambda x: datetime.strptime(x.strip(), '%Y-%m-%d %H:%M:%S'))
    latest_time = max(times, key=lambda x: datetime.strptime(x.strip(), '%Y-%m-%d %H:%M:%S'))
    net_difference = (datetime.strptime(latest_time.strip(), '%Y-%m-%d %H:%M:%S') -
                      datetime.strptime(earliest_time.strip(), '%Y-%m-%d %H:%M:%S'))
    return net_difference

if __name__ == '__main__':
    sample_times = '2023-01-01 12:00:00; 2023-01-01 14:30:00; 2023-01-01 10:00:00'
    result = calculate_net_time_difference(sample_times)
    print(result)