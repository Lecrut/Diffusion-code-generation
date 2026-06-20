def convert_seconds_to_hours(seconds):
    return seconds / 3600

if __name__ == '__main__':
    sample_duration = 45678
    print(convert_seconds_to_hours(sample_duration))