def convert_duration_to_human_readable(duration_str):
    parts = duration_str.split(':')
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
        parts_list.append(f"{days} Day{'s' if days != 1 else ''}")
    parts_list.append(f"{hours} Hour{'s' if hours != 1 else ''}")
    parts_list.append(f"{minutes} Minute{'s' if minutes != 1 else ''}")
    parts_list.append(f"{seconds} Second{'s' if seconds != 1 else ''}")

    return ', '.join(parts_list)

if __name__ == '__main__':
    print(convert_duration_to_human_readable("25:30:45"))
    print(convert_duration_to_human_readable("00:01:01"))
    print(convert_duration_to_human_readable("72:00:00"))
    print(convert_duration_to_human_readable("00:00:00"))