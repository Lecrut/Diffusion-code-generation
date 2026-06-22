from datetime import datetime

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

def calculate_duration(start_date: str, end_date: str, unit: str = 'human') -> str:
    fmt = '%Y-%m-%d %H:%M:%S'
    dt_start = datetime.strptime(start_date, fmt)
    dt_end = datetime.strptime(end_date, fmt)
    diff = dt_end - dt_start
    total_seconds = int(abs(diff.total_seconds()))
    
    if unit == 'seconds':
        return str(total_seconds)
    
    days = total_seconds // SECONDS_PER_DAY
    remainder = total_seconds % SECONDS_PER_DAY
    hours = remainder // SECONDS_PER_HOUR
    remainder = remainder % SECONDS_PER_HOUR
    minutes = remainder // SECONDS_PER_MINUTE
    seconds = remainder % SECONDS_PER_MINUTE
    
    components = []
    if days > 0:
        components.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        components.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        components.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not components:
        components.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return ', '.join(components)

if __name__ == '__main__':
    start = '2023-01-01 10:00:00'
    end = '2023-01-02 12:30:45'
    result_human = calculate_duration(start, end, 'human')
    result_seconds = calculate_duration(start, end, 'seconds')
    print(result_human)
    print(result_seconds)