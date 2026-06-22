HOURS_TO_SECONDS = 3600
MINUTES_TO_SECONDS = 60

def convert_to_total_seconds(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components must be non-negative")
    total_seconds = (hours * HOURS_TO_SECONDS +
                     minutes * MINUTES_TO_SECONDS +
                     seconds)
    return total_seconds

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 30
    sample_seconds = 45
    total_seconds = convert_to_total_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)