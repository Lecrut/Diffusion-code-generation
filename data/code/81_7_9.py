def convert_seconds_to_hours(total_seconds):
    return total_seconds / 3600

if __name__ == '__main__':
    sample_duration = 7265
    print(convert_seconds_to_hours(sample_duration))