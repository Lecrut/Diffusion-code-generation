def format_duration(total_seconds):
    total_seconds = int(total_seconds)
    if total_seconds < 0:
        return "-1 second"
    if total_seconds < 60:
        return f"1 second" if total_seconds == 1 else f"{total_seconds} seconds"
    if total_seconds < 3600:
        minutes, _ = divmod(total_seconds, 60)
        return f"1 minute" if minutes == 1 else f"{minutes} minutes"
    hours, remainder = divmod(total_seconds, 3600)
    if remainder < 60:
        return f"1 hour" if hours == 1 else f"{hours} hours"
    minutes, _ = divmod(remainder, 60)
    result_parts = []
    result_parts.append(f"1 hour" if hours == 1 else f"{hours} hours")
    result_parts.append(f"1 minute" if minutes == 1 else f"{minutes} minutes")
    return ", ".join(result_parts)

if __name__ == '__main__':
    print(format_duration(45))
    print(format_duration(90))
    print(format_duration(3600))
    print(format_duration(3661))
    print(format_duration(1))
    print(format_duration(0))