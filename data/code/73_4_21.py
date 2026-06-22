from datetime import datetime, timedelta

def calculate_duration(start_date: datetime, end_date: datetime, unit: str = 'human') -> str:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    
    if unit == 'seconds':
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
    start = datetime(2023, 1, 1, 10, 30, 0)
    end = datetime(2023, 1, 5, 14, 45, 30)
    
    print(calculate_duration(start, end, 'human'))
    print(calculate_duration(start, end, 'seconds'))