from datetime import datetime

def calculate_duration(start_date: datetime, end_date: datetime, unit: str = 'human') -> str:
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    
    if unit == 'seconds':
        return str(total_seconds)
    
    if unit == 'human':
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        hours = remaining // 3600
        remaining = remaining % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        
        parts = []
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} seconds")
            
        return ", ".join(parts)
    
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 10, 0, 0)
    end = datetime(2023, 1, 5, 14, 30, 45)
    
    print(calculate_duration(start, end, 'human'))
    print(calculate_duration(start, end, 'seconds'))