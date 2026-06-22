from datetime import datetime

def calculate_duration(start_date: str, end_date: str, unit: str = 'human') -> str:
    fmt = '%Y-%m-%d %H:%M:%S'
    dt_start = datetime.strptime(start_date, fmt)
    dt_end = datetime.strptime(end_date, fmt)
    diff = dt_end - dt_start
    abs_diff = abs(diff)
    total_secs = int(abs_diff.total_seconds())
    if unit == 'seconds':
        return str(total_secs)
    days = total_secs // 86400
    hours = (total_secs % 86400) // 3600
    minutes = (total_secs % 3600) // 60
    seconds = total_secs % 60
    parts = []
    if days:
        label = 'day' if days == 1 else 'days'
        parts.append(f"{days} {label}")
    if hours:
        label = 'hour' if hours == 1 else 'hours'
        parts.append(f"{hours} {label}")
    if minutes:
        label = 'minute' if minutes == 1 else 'minutes'
        parts.append(f"{minutes} {label}")
    if seconds or not parts:
        label = 'second' if seconds == 1 else 'seconds'
        parts.append(f"{seconds} {label}")
    return ', '.join(parts)

if __name__ == '__main__':
    result = calculate_duration('2023-01-01 10:00:00', '2023-01-02 12:30:45', 'human')
    print(result)
    result_seconds = calculate_duration('2023-01-01 10:00:00', '2023-01-02 12:30:45', 'seconds')
    print(result_seconds)