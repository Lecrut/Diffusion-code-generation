def convert_seconds_to_hours(total_seconds):
    return total_seconds / 3600.0

if __name__ == '__main__':
    sample_duration = 7261
    elapsed_hours = convert_seconds_to_hours(sample_duration)
    print(elapsed_hours)