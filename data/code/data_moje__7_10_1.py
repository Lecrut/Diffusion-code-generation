def convert_duration(value, unit):
    if value < 0:
        raise ValueError("Value must be non-negative")
    
    seconds = 0
    if unit == 'seconds':
        seconds = value
    elif unit == 'minutes':
        seconds = value * 60
    elif unit == 'hours':
        seconds = value * 3600
    elif unit == 'days':
        seconds = value * 86400
    else:
        raise ValueError("Invalid unit specified")
    
    days = int(seconds // 86400)
    remaining = seconds % 86400
    hours = int(remaining // 3600)
    remaining = remaining % 3600
    minutes = int(remaining // 60)
    secs = int(remaining % 60)
    
    total_days = seconds / 86400
    total_hours = seconds / 3600
    total_minutes = seconds / 60
    
    return {
        'seconds': seconds,
        'minutes': total_minutes,
        'hours': total_hours,
        'days': total_days,
        'formatted': f"{days}d {hours}h {minutes}m {secs}s"
    }

if __name__ == '__main__':
    result = convert_duration(90061, 'seconds')
    print(result)