from datetime import datetime

def calculate_net_time_difference(time_differences: str) -> str:
    times = time_differences.split(';')
    parsed_times = [datetime.strptime(time.strip(), '%Y-%m-%d %H:%M:%S') for time in times]
    earliest_time = min(parsed_times)
    latest_time = max(parsed_times)
    net_difference = latest_time - earliest_time
    return str(net_difference)
if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00; 2023-01-02 14:30:00; 2023-01-01 09:00:00'
    result = calculate_net_time_difference(sample_input)
    print(result)