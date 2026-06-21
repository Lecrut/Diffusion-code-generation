def convert_time_to_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_hours = 5
    sample_minutes = 20
    sample_seconds = 15
    total_seconds = convert_time_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)