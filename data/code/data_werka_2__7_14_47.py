def validate_input(days, hours, minutes, seconds):
    if not all(isinstance(i, int) for i in (days, hours, minutes, seconds)):
        raise ValueError("All inputs must be integers.")
    if any(i < 0 for i in (days, hours, minutes, seconds)):
        raise ValueError("All inputs must be non-negative.")

def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    validate_input(days, hours, minutes, seconds)
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds // 60

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 45
    sample_seconds = 30
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)