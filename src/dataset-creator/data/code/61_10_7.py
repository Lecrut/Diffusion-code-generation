def convert_seconds_to_hms(seconds):
    if seconds < 0:
        raise ValueError("Input must be non-negative")
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours} hours, {minutes} minutes and {remaining_seconds} seconds"
if __name__ == '__main__':
    sample_values = [3725, 4891, 60]
    for val in sample_values:
        print(f"Input: {val}")