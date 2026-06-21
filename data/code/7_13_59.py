HOURS_TO_SECONDS = 3600
MINUTES_TO_SECONDS = 60

def convert_to_seconds(hours, minutes, seconds):
    return hours * HOURS_TO_SECONDS + minutes * MINUTES_TO_SECONDS + seconds

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 59
    sample_seconds = 59
    total_seconds = convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)