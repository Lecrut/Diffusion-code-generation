def format_time(total_seconds):
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be a number")
    
    total_seconds = int(total_seconds)
    
    if total_seconds < 0:
        raise ValueError("Input must be non-negative")
    
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    if hours > 0:
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes, {seconds} seconds"
    else:
        return f"{seconds} seconds"

if __name__ == '__main__':
    print(format_time(3661))
    print(format_time(95))
    print(format_time(45))
    print(format_time(86400))
    print(format_time(0))