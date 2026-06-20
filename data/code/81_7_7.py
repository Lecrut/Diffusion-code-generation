def convert_seconds_to_hours(total_seconds):
    return total_seconds / 3600

if __name__ == '__main__':
    sample_duration = 7259
    hours_elapsed = convert_seconds_to_hours(sample_duration)
    print(hours_elapsed)