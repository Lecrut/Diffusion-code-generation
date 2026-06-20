def convert_seconds_to_hours(total_seconds):
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Total seconds must be a non-negative number")
    return total_seconds / 3600.0

if __name__ == '__main__':
    sample_duration = 7261
    print(convert_seconds_to_hours(sample_duration))