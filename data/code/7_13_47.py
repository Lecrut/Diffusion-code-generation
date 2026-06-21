def convert_to_seconds(hours, minutes, seconds):
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    
    total_seconds = (hours * SECONDS_PER_HOUR +
                     minutes * SECONDS_PER_MINUTE +
                     seconds)
    return total_seconds

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 30
    sample_seconds = 45
    total_seconds = convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)