def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    if not all(isinstance(i, int) and i >= 0 for i in (days, hours, minutes, seconds)):
        raise ValueError("All inputs must be non-negative integers.")
    
    MINUTES_PER_DAY = 24 * 60
    MINUTES_PER_HOUR = 60
    
    total_minutes = (days * MINUTES_PER_DAY) + (hours * MINUTES_PER_HOUR) + minutes + (seconds // 60)
    return total_minutes

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 45
    sample_seconds = 30
    try:
        result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
        print(result)
    except ValueError as e:
        print(e)