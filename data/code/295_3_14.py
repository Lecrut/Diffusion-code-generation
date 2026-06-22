def validate_hours(hours):
    if not isinstance(hours, int) or hours < 0:
        raise ValueError("Hours must be a non-negative integer")
    return hours

def convert_to_minutes_and_seconds(hours):
    minutes = hours * 60
    seconds = 0
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    try:
        sample_hours = validate_hours(3)
        result = convert_to_minutes_and_seconds(sample_hours)
        print(result)
    except ValueError as e:
        print(e)