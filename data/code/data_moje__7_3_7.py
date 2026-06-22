def format_duration(duration_string):
    try:
        parts = duration_string.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid format")
        hours_total = int(parts[0])
        minutes_total = int(parts[1])
        seconds_total = int(parts[2])
        total_seconds = hours_total * 3600 + minutes_total * 60 + seconds_total
        days = total_seconds // 86400
        remainder = total_seconds % 86400
        hours = remainder // 3600
        remainder %= 3600
        minutes = remainder // 60
        seconds = remainder % 60
        result_parts = []
        if days > 0:
            result_parts.append(f"{days} Day{'s' if days != 1 else ''}")
        if hours > 0:
            result_parts.append(f"{hours} Hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            result_parts.append(f"{minutes} Minute{'s' if minutes != 1 else ''}")
        if seconds > 0 or len(result_parts) == 0:
            result_parts.append(f"{seconds} Second{'s' if seconds != 1 else ''}")
        return ", ".join(result_parts)
    except Exception:
        return "Invalid duration format"

if __name__ == '__main__':
    sample_values = ["00:00:00", "01:30:45", "25:15:10", "48:00:00", "00:01:00"]
    for val in sample_values:
        print(f"{val} -> {format_duration(val)}")