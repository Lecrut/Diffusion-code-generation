def convert_seconds(total_seconds: int) -> str:
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        if remainder == 0:
            return f"{hours} hours"
        if remainder >= 60:
            minutes = remainder // 60
            seconds = remainder % 60
            return f"{hours} hours, {minutes} minutes, {seconds} seconds"
        return f"{hours} hours, {remainder} seconds"
    if total_seconds >= 60:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        if seconds == 0:
            return f"{minutes} minutes"
        return f"{minutes} minutes, {seconds} seconds"
    return f"{total_seconds} seconds"

if __name__ == '__main__':
    test_values = [5, 120, 3700, 86400, 0, 60]
    for val in test_values:
        print(convert_seconds(val))