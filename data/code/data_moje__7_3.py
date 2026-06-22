import datetime

def convert_duration(duration_str: str) -> str:
    total_seconds = 0
    parts = duration_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    parts_out = []
    if days > 0:
        parts_out.append(f"{days} days")
    if hours > 0:
        parts_out.append(f"{hours} hours")
    if minutes > 0:
        parts_out.append(f"{minutes} minutes")
    if seconds > 0 or not parts_out:
        parts_out.append(f"{seconds} seconds")
    
    return ', '.join(parts_out)

if __name__ == '__main__':
    duration = "25:01:02"
    result = convert_duration(duration)
    print(result)