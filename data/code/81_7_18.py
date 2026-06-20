def seconds_to_hours(total_seconds):
    return total_seconds / 3600.0

if __name__ == '__main__':
    sample_duration = 3661
    print(seconds_to_hours(sample_duration))