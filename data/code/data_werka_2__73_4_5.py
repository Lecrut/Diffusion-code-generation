from datetime import datetime

def calculate_duration(start_date: str, end_date: str, unit: str = 'human') -> str:
    fmt = '%Y-%m-%d %H:%M:%S'
    start = datetime.strptime(start_date, fmt)
    end = datetime.strptime(end_date, fmt)
    delta = end - start
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
        parts.append(f'{days} day' + ('s' if days != 1 else ''))
    if hours > 0:
        parts.append(f'{hours} hour' + ('s' if hours != 1 else ''))
    if minutes > 0:
        parts.append(f'{minutes} minute' + ('s' if minutes != 1 else ''))
    if seconds > 0 or not parts:
        parts.append(f'{seconds} second' + ('s' if seconds != 1 else ''))
    return ', '.join(parts)

if __name__ == '__main__':
    result = calculate_duration('2023-01-01 00:00:00', '2023-01-02 01:02:03', 'human')
    print(result)
    result_seconds = calculate_duration('2023-01-01 00:00:00', '2023-01-02 01:02:03', 'seconds')
    print(result_seconds)