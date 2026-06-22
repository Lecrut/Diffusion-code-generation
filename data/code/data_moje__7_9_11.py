import datetime

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime, unit: str) -> float:
    delta = end - start
    total_seconds = abs(delta.total_seconds())
    
    if unit == "seconds":
        return total_seconds
    if unit == "minutes":
        return total_seconds / 60
    if unit == "hours":
        return total_seconds / 3600
    if unit == "days":
        return total_seconds / 86400
    if unit == "weeks":
        return total_seconds / 604800
    
    raise ValueError(f"Unsupported unit: {unit}")

def format_time_difference(start: datetime.datetime, end: datetime.datetime) -> str:
    delta = end - start
    total_seconds = int(abs(delta.total_seconds()))
    
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
        
    return " ".join(parts)

if __name__ == "__main__":
    start_time = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime.datetime(2023, 1, 5, 14, 30, 45)
    
    difference_in_hours = calculate_time_difference(start_time, end_time, "hours")
    print(f"Time difference in hours: {difference_in_hours}")
    
    formatted_difference = format_time_difference(start_time, end_time)
    print(f"Formatted difference: {formatted_difference}")