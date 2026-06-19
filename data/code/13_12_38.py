from datetime import datetime

def calculate_net_time_difference(time_string):
    times = time_string.split(';')
    earliest_time = min(times, key=lambda x: datetime.strptime(x.strip(), '%H:%M'))
    latest_time = max(times, key=lambda x: datetime.strptime(x.strip(), '%H:%M'))
    net_difference = (datetime.strptime(latest_time.strip(), '%H:%M') - 
                      datetime.strptime(earliest_time.strip(), '%H:%M')).seconds // 3600
    return net_difference

if __name__ == '__main__':
    sample_input = "09:00;12:30;15:45;08:15"
    result = calculate_net_time_difference(sample_input)
    print(result)