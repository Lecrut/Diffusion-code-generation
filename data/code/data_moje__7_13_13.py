def time_string_to_readable(time_string):
    try:
        parts = time_string.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid format")
        
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError("Values out of range")
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        
        hours_out = remaining // 3600
        remaining %= 3600
        
        minutes_out = remaining // 60
        seconds_out = remaining % 60
        
        parts_out = []
        if days > 0:
            parts_out.append(f"{days} days" if days > 1 else f"{days} day")
        if hours_out > 0:
            parts_out.append(f"{hours_out} hours" if hours_out > 1 else f"{hours_out} hour")
        if minutes_out > 0:
            parts_out.append(f"{minutes_out} minutes" if minutes_out > 1 else f"{minutes_out} minute")
        if seconds_out > 0:
            parts_out.append(f"{seconds_out} seconds" if seconds_out > 1 else f"{seconds_out} second")
        
        if not parts_out:
            return "0 seconds"
        
        if len(parts_out) == 1:
            return parts_out[0]
        elif len(parts_out) == 2:
            return f"{parts_out[0]} and {parts_out[1]}"
        else:
            return ", ".join(parts_out[:-1]) + f" and {parts_out[-1]}"
            
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    sample_input = "01:15:30"
    result = time_string_to_readable(sample_input)
    print(result)
    
    sample_input2 = "48:30:00"
    result2 = time_string_to_readable(sample_input2)
    print(result2)
    
    sample_input3 = "00:00:05"
    result3 = time_string_to_readable(sample_input3)
    print(result3)