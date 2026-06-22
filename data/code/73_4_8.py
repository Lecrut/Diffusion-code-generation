from datetime import datetime

def calculate_duration(start_date: str, end_date: str, format_type: str = 'human_readable') -> str:
    fmt = '%Y-%m-%d %H:%M:%S'
    start_dt = datetime.strptime(start_date, fmt)
    end_dt = datetime.strptime(end_date, fmt)
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds = -total_seconds
    if format_type == 'seconds':
        return str(total_seconds)
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    return ', '.join(parts)

if __name__ == '__main__':
    start = '2023-01-01 00:00:00'
    end = '2023-01-02 01:02:03'
    print(calculate_duration(start, end, 'human_readable'))
    print(calculate_duration(start, end, 'seconds'))