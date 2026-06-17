def convert_seconds_to_hms(seconds):
    if seconds < 0:
        return None
    hours = seconds // 3600
    remaining_minutes = (seconds % 3600) // 60
    minutes = remaining_minutes
    return f"{hours}h {minutes}m"
if __name__ == '__main__':
    sample_seconds = 7245
    result = convert_seconds_to_hms(sample_seconds)
    print(result)