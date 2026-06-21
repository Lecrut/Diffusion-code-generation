from datetime import datetime

def calculate_net_time_difference(time_differences: str) -> str:
    times = time_differences.split(';')
    if not times or len(times) < 2:
        raise ValueError('At least two time points are required.')
    try:
        parsed_times = [datetime.fromisoformat(time.strip()) for time in times]
    except ValueError as e:
        raise ValueError('Invalid time format. Please use ISO 8601 format.') from e
    earliest_time = min(parsed_times)
    latest_time = max(parsed_times)
    net_difference = latest_time - earliest_time
    return str(net_difference)
if __name__ == '__main__':
    sample_input = '2023-10-01T12:00:00;2023-10-01T15:30:00;2023-10-01T09:45:00'
    result = calculate_net_time_difference(sample_input)
    print(result)