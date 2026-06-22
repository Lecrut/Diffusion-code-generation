def convert_seconds(seconds):
    if seconds >= 3600:
        hours = seconds // 3600
        remaining = seconds % 3600
        if remaining >= 60:
            minutes = remaining // 60
            secs = remaining % 60
            return f"{hours}h {minutes}m {secs}s"
        else:
            return f"{hours}h {remaining}s"
    elif seconds >= 60:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}m {secs}s"
    else:
        return f"{seconds}s"

if __name__ == '__main__':
    print(convert_seconds(3661))
    print(convert_seconds(125))
    print(convert_seconds(45))