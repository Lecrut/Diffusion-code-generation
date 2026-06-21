from typing import List

def parse_time_difference(time_str: str) -> int:

    def parse_component(value: str, unit: str) -> int:
        if not value.isdigit():
            raise ValueError(f'Invalid numeric value: {value}')
        value = int(value)
        if unit == 'hour':
            return value * 60
        elif unit == 'minute':
            return value
        else:
            raise ValueError(f'Unsupported time unit: {unit}')
    parts = time_str.split()
    total_minutes = 0
    for i in range(0, len(parts), 2):
        if i + 1 >= len(parts):
            raise ValueError('Malformed time difference string')
        value = parts[i]
        unit = parts[i + 1].lower().rstrip('s')
        total_minutes += parse_component(value, unit)
    return total_minutes

def total_elapsed_time(time_differences: List[str]) -> int:
    if not isinstance(time_differences, list):
        raise ValueError('Input must be a list of time difference strings')
    total_time = sum((parse_time_difference(td) for td in time_differences))
    return total_time
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '4 hours']
    try:
        total_time = total_elapsed_time(sample_times)
        print(total_time)
    except ValueError as e:
        print(f'Error: {e}')