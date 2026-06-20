def convert_seconds_to_hours(seconds):
    return seconds / 3600.0

if __name__ == '__main__':
    sample_duration = 7265
    print(convert_seconds_to_hours(sample_duration))