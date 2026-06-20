def format_seconds(total_seconds):
    total_seconds = int(total_seconds)
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        secs = remaining % 60
        if minutes > 0 or secs > 0:
            return f"{hours} hour(s), {minutes} minute(s), {secs} second(s)"
        else:
            return f"{hours} hour(s)"
    elif total_seconds >= 60:
        minutes = total_seconds // 60
        secs = total_seconds % 60
        if secs > 0:
            return f"{minutes} minute(s), {secs} second(s)"
        else:
            return f"{minutes} minute(s)"
    else:
        return f"{total_seconds} second(s)"

if __name__ == '__main__':
    print(format_seconds(3661))
    print(format_seconds(125))
    print(format_seconds(45))
    print(format_seconds(7200))