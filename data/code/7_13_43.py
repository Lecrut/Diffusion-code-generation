def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    sample_hours = 2
    sample_minutes = 45
    sample_seconds = 30
    total_seconds = time_to_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)