def convert_to_total_seconds(hours, minutes, seconds):
    hours_to_seconds = hours * 3600
    minutes_to_seconds = minutes * 60
    total_seconds = hours_to_seconds + minutes_to_seconds + seconds
    return total_seconds

if __name__ == '__main__':
    sample_hours = 1
    sample_minutes = 59
    sample_seconds = 59
    total_seconds = convert_to_total_seconds(sample_hours, sample_minutes, sample_seconds)
    print(total_seconds)