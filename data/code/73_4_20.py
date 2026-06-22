from datetime import datetime

def calculate_duration(start_date: datetime, end_date: datetime, unit: str = 'human') -> str:
    if not isinstance(unit, str) or unit not in ('seconds', 'human'):
        raise ValueError("Unit must be 'seconds' or 'human'")
    
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Dates must be datetime objects")
    
    delta = end_date - start_date
    abs_delta = abs(delta)
    total_seconds = int(abs_delta.total_seconds())
    
    if unit == 'seconds':
        return str(total_seconds)
    
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    
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
    start = datetime(2023, 10, 1, 10, 0, 0)
    end = datetime(2023, 10, 5, 14, 30, 45)
    result_human = calculate_duration(start, end, 'human')
    result_seconds = calculate_duration(start, end, 'seconds')
    print(result_human)
    print(result_seconds)