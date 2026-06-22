from datetime import datetime, timedelta

def calculate_duration(start_date, end_date, unit='human'):
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object")
    if unit not in ('seconds', 'human'):
        raise ValueError("unit must be 'seconds' or 'human'")
    
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    
    if unit == 'seconds':
        return str(total_seconds)
    
    if total_seconds < 0:
        total_seconds = -total_seconds
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    
    parts = []
    if days > 0:
        label = 'day' if days == 1 else 'days'
        parts.append(f"{days} {label}")
    if hours > 0:
        label = 'hour' if hours == 1 else 'hours'
        parts.append(f"{hours} {label}")
    if minutes > 0:
        label = 'minute' if minutes == 1 else 'minutes'
        parts.append(f"{minutes} {label}")
    if seconds > 0 or not parts:
        label = 'second' if seconds == 1 else 'seconds'
        parts.append(f"{seconds} {label}")
    
    return ", ".join(parts)

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 10, 30, 0)
    end = datetime(2023, 1, 5, 14, 45, 30)
    result = calculate_duration(start, end, 'human')
    print(result)
    result_sec = calculate_duration(start, end, 'seconds')
    print(result_sec)