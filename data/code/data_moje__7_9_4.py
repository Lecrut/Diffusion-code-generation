import datetime

def calculate_time_difference(start_time, end_time, unit="days"):
    if start_time > end_time:
        raise ValueError("Start time must be before or equal to end time.")
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if unit == "days":
        result = total_seconds / 86400
        return result
    elif unit == "hours":
        result = total_seconds / 3600
        return result
    elif unit == "minutes":
        result = total_seconds / 60
        return result
    elif unit == "seconds":
        result = total_seconds
        return result
    elif unit == "mixed":
        total_minutes = int(total_seconds // 60)
        remaining_seconds = int(total_seconds % 60)
        days = total_minutes // 1440
        remaining_minutes = total_minutes % 1440
        hours = remaining_minutes // 60
        final_minutes = remaining_minutes % 60
        return {
            "days": days,
            "hours": hours,
            "minutes": final_minutes,
            "seconds": remaining_seconds
        }
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == "__main__":
    start = datetime.datetime(2023, 1, 1, 8, 30, 0)
    end = datetime.datetime(2023, 1, 3, 14, 45, 30)
    
    days_diff = calculate_time_difference(start, end, "days")
    hours_diff = calculate_time_difference(start, end, "hours")
    mixed_diff = calculate_time_difference(start, end, "mixed")
    
    print(f"Total days: {days_diff}")
    print(f"Total hours: {hours_diff}")
    print(f"Mixed format: {mixed_diff}")