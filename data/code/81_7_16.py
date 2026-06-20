def seconds_to_hours(seconds):
    hours = seconds / 3600.0
    return hours

if __name__ == '__main__':
    sample_duration = 12345
    elapsed_hours = seconds_to_hours(sample_duration)
    print(elapsed_hours)