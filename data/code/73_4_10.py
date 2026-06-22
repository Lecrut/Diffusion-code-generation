from datetime import datetime, timedelta

def calculate_duration(start_date, end_date, unit='human'):
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects")
    
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    
    if unit == 'seconds':
        return total_seconds
    elif unit == 'human':
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
            
        return ", ".join(parts)
    else:
        raise ValueError("unit must be 'seconds' or 'human'")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 10, 30, 0)
    end = datetime(2023, 1, 5, 14, 45, 30)
    
    print(calculate_duration(start, end, 'seconds'))
    print(calculate_duration(start, end, 'human'))