def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("All input values must be non-negative integers.")
    
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds // 60

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 15
    sample_seconds = 50
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)