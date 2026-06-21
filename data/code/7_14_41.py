def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds // 60

if __name__ == '__main__':
    sample_days = 1
    sample_hours = 5
    sample_minutes = 30
    sample_seconds = 45
    
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)