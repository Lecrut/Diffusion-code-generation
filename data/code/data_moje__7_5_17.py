def convert_time(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        secs = remaining % 60
        if minutes > 0 or secs > 0:
            return f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}, {secs} second{'s' if secs != 1 else ''}"
        return f"{hours} hour{'s' if hours != 1 else ''}"
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        remaining = total_seconds % 60
        return f"{minutes} minute{'s' if minutes != 1 else ''}, {remaining} second{'s' if remaining != 1 else ''}"
    else:
        return f"{total_seconds} second{'s' if total_seconds != 1 else ''}"

if __name__ == '__main__':
    print(convert_time(3661))
    print(convert_time(125))
    print(convert_time(90))
    print(convert_time(1))
    print(convert_time(60))