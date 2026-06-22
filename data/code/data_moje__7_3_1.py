def convert_duration(duration_string):
    parts = duration_string.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    total_seconds %= 86400
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    result = []
    if days > 0:
        result.append(f"{days} Day" + ("s" if days != 1 else ""))
    if hours > 0:
        result.append(f"{hours} Hour" + ("s" if hours != 1 else ""))
    if minutes > 0:
        result.append(f"{minutes} Minute" + ("s" if minutes != 1 else ""))
    if seconds > 0:
        result.append(f"{seconds} Second" + ("s" if seconds != 1 else ""))
    if not result:
        result.append("0 Seconds")
    return ", ".join(result)

if __name__ == '__main__':
    sample1 = "00:00:00"
    sample2 = "01:02:03"
    sample3 = "25:30:45"
    sample4 = "72:15:10"
    print(convert_duration(sample1))
    print(convert_duration(sample2))
    print(convert_duration(sample3))
    print(convert_duration(sample4))