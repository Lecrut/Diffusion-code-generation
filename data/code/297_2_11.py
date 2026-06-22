def validate_input(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Input must be a non-negative integer")

def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}h {minutes}m {remaining_seconds}s"

if __name__ == '__main__':
    sample_seconds = 7845
    validate_input(sample_seconds)
    print(convert_seconds_to_hms(sample_seconds))