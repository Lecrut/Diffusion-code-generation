def convert_seconds(total_seconds):
    if total_seconds < 0:
        raise ValueError("Seconds must be non-negative")
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

if __name__ == '__main__':
    print(convert_seconds(3661))
    print(convert_seconds(185))
    print(convert_seconds(45))
    print(convert_seconds(7200))
    print(convert_seconds(0))