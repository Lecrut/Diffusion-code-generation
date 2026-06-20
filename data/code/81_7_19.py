SECONDS_PER_HOUR = 3600

def convert_seconds_to_hours(total_seconds):
    return total_seconds / SECONDS_PER_HOUR

if __name__ == '__main__':
    sample_duration = 3665
    elapsed_hours = convert_seconds_to_hours(sample_duration)
    print(elapsed_hours)