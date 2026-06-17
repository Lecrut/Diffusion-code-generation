from datetime import datetime
def time_diff_to_string(time_str1: str, time_str2: str) -> str:
    time_format = "%H:%M"
    try:
        dt1 = datetime.strptime(time_str1, time_format)
        dt2 = datetime.strptime(time_str2, time_format)
    except ValueError:
        return "Error: Invalid time format"
    diff = abs(dt1 - dt2)
    total_seconds = int(diff.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if not parts:
        return "0 minutes"
    if len(parts) == 1:
        return parts[0]
    else:
        return f"{parts[0]}, {parts[1]}"
if __name__ == '__main__':
    time_a = "14:30"
    time_b = "16:05"
    result1 = time_diff_to_string(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1}")
    time_c = "09:00"
    time_d = "08:45"
    result2 = time_diff_to_string(time_c, time_d)
    print(f"Difference between {time_c} and {time_d}: {result2}")
    time_e = "23:59"
    time_f = "00:01"
    result3 = time_diff_to_string(time_e, time_f)
    print(f"Difference between {time_e} and {time_f}: {result3}")
    time_g = "10:15"
    time_h = "10:15"
    result4 = time_diff_to_string(time_g, time_h)
    print(f"Difference between {time_g} and {time_h}: {result4}")