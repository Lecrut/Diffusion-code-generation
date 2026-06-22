SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def convert_to_total_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    return (hours * SECONDS_PER_HOUR +
            minutes * SECONDS_PER_MINUTE +
            seconds)

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 30
    sample_seconds = 45
    total_seconds = convert_to_total_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)