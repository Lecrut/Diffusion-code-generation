def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    MINUTES_IN_DAY = 24 * 60
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    total_seconds = (days * MINUTES_IN_DAY * SECONDS_IN_MINUTE) + \
                   (hours * MINUTES_IN_HOUR * SECONDS_IN_MINUTE) + \
                   (minutes * SECONDS_IN_MINUTE) + seconds
    
    return total_seconds // SECONDS_IN_MINUTE

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 40
    sample_seconds = 50
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)