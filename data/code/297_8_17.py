def validate_minutes(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError('Invalid input: value must be a non-negative number of minutes')

def minutes_to_days(minutes):
    return minutes / 1440.0
if __name__ == '__main__':
    sample_minutes = 1440
    validate_minutes(sample_minutes)
    days = minutes_to_days(sample_minutes)
    print(days)