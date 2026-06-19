from datetime import datetime

def calculate_net_time_difference(time_string):
    times = time_string.split(';')
    earliest_time = min(times, key=lambda x: datetime.strptime(x.strip(), '%H:%M'))
    latest_time = max(times, key=lambda x: datetime.strptime(x.strip(), '%H:%M'))
    net_difference = (datetime.strptime(latest_time.strip(), '%H:%M') - 
                      datetime.strptime(earliest_time.strip(), '%H:%M')).seconds
    return net_difference

if __name__ == '__main__':
    sample_times = "09:15; 14:30; 08:45; 20:00"
    print(calculate_net_time_difference(sample_times))