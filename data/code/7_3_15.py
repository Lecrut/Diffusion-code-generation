def format_duration(time_string):
    parts = time_string.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    parts_list = []
    if days > 0:
        if days == 1:
            parts_list.append("1 Day")
        else:
            parts_list.append(f"{days} Days")
    if hours > 0:
        if hours == 1:
            parts_list.append("1 Hour")
        else:
            parts_list.append(f"{hours} Hours")
    if minutes > 0:
        if minutes == 1:
            parts_list.append("1 Minute")
        else:
            parts_list.append(f"{minutes} Minutes")
    if seconds > 0 or not parts_list:
        if seconds == 1:
            parts_list.append("1 Second")
        else:
            parts_list.append(f"{seconds} Seconds")

    return ", ".join(parts_list)

if __name__ == '__main__':
    print(format_duration("25:30:45"))
    print(format_duration("00:00:00"))
    print(format_duration("01:01:01"))
    print(format_duration("48:00:00"))
    print(format_duration("00:00:59"))