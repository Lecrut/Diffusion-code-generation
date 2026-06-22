def time_string_to_human_readable(time_str):
    parts = time_str.split(':')
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
    if days > 0:
        day_part = f"{days} days" if days == 1 else f"{days} days"
        if hours > 0:
            hour_part = f"{hours} hours" if hours == 1 else f"{hours} hours"
            if minutes > 0:
                minute_part = f"{minutes} minutes" if minutes == 1 else f"{minutes} minutes"
                if seconds > 0:
                    second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
                    return f"{day_part}, {hour_part}, {minute_part}, {second_part}"
                return f"{day_part}, {hour_part}, {minute_part}"
            if seconds > 0:
                second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
                return f"{day_part}, {second_part}"
            return day_part
        if minutes > 0:
            minute_part = f"{minutes} minutes" if minutes == 1 else f"{minutes} minutes"
            if seconds > 0:
                second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
                return f"{day_part}, {minute_part}, {second_part}"
            return f"{day_part}, {minute_part}"
        if seconds > 0:
            second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
            return f"{day_part}, {second_part}"
        return day_part
    if hours > 0:
        hour_part = f"{hours} hours" if hours == 1 else f"{hours} hours"
        if minutes > 0:
            minute_part = f"{minutes} minutes" if minutes == 1 else f"{minutes} minutes"
            if seconds > 0:
                second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
                return f"{hour_part}, {minute_part}, {second_part}"
            return f"{hour_part}, {minute_part}"
        if seconds > 0:
            second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
            return f"{hour_part}, {second_part}"
        return hour_part
    if minutes > 0:
        minute_part = f"{minutes} minutes" if minutes == 1 else f"{minutes} minutes"
        if seconds > 0:
            second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
            return f"{minute_part}, {second_part}"
        return minute_part
    if seconds > 0:
        second_part = f"{seconds} seconds" if seconds == 1 else f"{seconds} seconds"
        return second_part
    return "0 seconds"

if __name__ == '__main__':
    print(time_string_to_human_readable("25:30:45"))
    print(time_string_to_human_readable("00:01:00"))
    print(time_string_to_human_readable("00:00:00"))
    print(time_string_to_human_readable("72:00:00"))
    print(time_string_to_human_readable("01:02:03"))