from datetime import datetime, timedelta

def calculate_duration(start_date, end_date, unit='human'):
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    
    delta = end_date - start_date
    abs_delta = abs(delta)
    total_seconds = int(abs_delta.total_seconds())
    
    if unit == 'seconds':
        return str(total_seconds)
    
    if unit != 'human':
        raise ValueError(f"Unsupported unit: {unit}")
    
    units_map = {
        'day': 86400,
        'hour': 3600,
        'minute': 60,
        'second': 1
    }
    
    parts = []
    remaining = total_seconds
    
    for unit_name, unit_seconds in units_map.items():
        if remaining >= unit_seconds:
            count = remaining // unit_seconds
            remaining %= unit_seconds
            plural = 's' if count != 1 else ''
            parts.append(f"{count} {unit_name}{plural}")
    
    if not parts:
        return "0 seconds"
    
    return ', '.join(parts)

if __name__ == '__main__':
    start = '2023-01-01 10:00:00'
    end = '2023-01-05 14:30:45'
    
    result_seconds = calculate_duration(start, end, 'seconds')
    print(result_seconds)
    
    result_human = calculate_duration(start, end, 'human')
    print(result_human)