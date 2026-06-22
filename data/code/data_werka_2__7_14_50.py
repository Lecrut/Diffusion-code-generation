def convert_to_minutes(days, hours, minutes, seconds):
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes + (seconds / 60)
    return total_minutes

if __name__ == '__main__':
    sample_days = 1
    sample_hours = 3
    sample_minutes = 45
    sample_seconds = 30
    
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)