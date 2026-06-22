def convert_to_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    sample_hours = 2
    sample_minutes = 45
    sample_seconds = 30
    result = convert_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(result)