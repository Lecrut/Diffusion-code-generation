from datetime import datetime
def time_diff_to_string(time_str1: str, time_str2: str) -> str:
    time_format = "%H:%M"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    diff = time2 - time1
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
        return ", ".join(parts)
if __name__ == '__main__':
    t1 = "14:30"
    t2 = "17:05"
    result = time_diff_to_string(t1, t2)
    print(f"{t1} to {t2}: {result}")
    t3 = "09:00"
    t4 = "11:15"
    result2 = time_diff_to_string(t3, t4)
    print(f"{t3} to {t4}: {result2}")
    t5 = "23:59"
    t6 = "00:01"
    result3 = time_diff_to_string(t5, t6)
    print(f"{t5} to {t6}: {result3}")
    t7 = "10:00"
    t8 = "10:00"
    result4 = time_diff_to_string(t7, t8)
    print(f"{t7} to {t8}: {result4}")