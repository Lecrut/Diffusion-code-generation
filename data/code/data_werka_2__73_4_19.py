from datetime import datetime, timedelta

def calculate_duration(date1_str, date2_str, unit='human'):
    fmt = '%Y-%m-%d %H:%M:%S'
    dt1 = datetime.strptime(date1_str, fmt)
    dt2 = datetime.strptime(date2_str, fmt)
    delta = dt2 - dt1
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds = -total_seconds
    if unit == 'seconds':
        return total_seconds
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    parts = []
    if days > 0:
        parts.append(f'{days} day{"s" if days != 1 else ""}')
    if hours > 0:
        parts.append(f'{hours} hour{"s" if hours != 1 else ""}')
    if minutes > 0:
        parts.append(f'{minutes} minute{"s" if minutes != 1 else ""}')
    if seconds > 0 or not parts:
        parts.append(f'{seconds} second{"s" if seconds != 1 else ""}')
    return ', '.join(parts)

if __name__ == '__main__':
    start_date = '2023-01-01 00:00:00'
    end_date = '2023-01-02 12:30:45'
    print(calculate_duration(start_date, end_date, 'human'))
    print(calculate_duration(start_date, end_date, 'seconds'))