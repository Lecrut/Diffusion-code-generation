from datetime import datetime

def calculate_duration(start_date: str, end_date: str, unit: str = 'human') -> str:
    fmt = '%Y-%m-%d %H:%M:%S'
    start_dt = datetime.strptime(start_date, fmt)
    end_dt = datetime.strptime(end_date, fmt)
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds = -total_seconds
    if unit == 'seconds':
        return str(total_seconds)
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    parts = []
    if days > 0:
        parts.append(f'{days} days')
    if hours > 0:
        parts.append(f'{hours} hours')
    if minutes > 0:
        parts.append(f'{minutes} minutes')
    if seconds > 0 or not parts:
        parts.append(f'{seconds} seconds')
    return ', '.join(parts)

if __name__ == '__main__':
    start = '2023-01-01 00:00:00'
    end = '2023-01-02 01:02:03'
    print(calculate_duration(start, end, 'human'))
    print(calculate_duration(start, end, 'seconds'))