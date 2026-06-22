def convert_time(total_seconds):
    total_seconds = int(total_seconds)
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        secs = remaining % 60
        if hours == 1:
            return f"1 hour"
        else:
            if minutes == 0 and secs == 0:
                return f"{hours} hours"
            if minutes == 0:
                return f"{hours} hours and {secs} seconds"
            return f"{hours} hours, {minutes} minutes, and {secs} seconds"
    
    if total_seconds >= 60:
        minutes = total_seconds // 60
        remaining = total_seconds % 60
        if minutes == 1:
            return f"1 minute"
        else:
            if remaining == 0:
                return f"{minutes} minutes"
            return f"{minutes} minutes and {remaining} seconds"
    
    if total_seconds == 1:
        return "1 second"
    return f"{total_seconds} seconds"

if __name__ == '__main__':
    samples = [0, 5, 60, 120, 3600, 3661, 90061]
    for sec in samples:
        print(f"{sec}s -> {convert_time(sec)}")