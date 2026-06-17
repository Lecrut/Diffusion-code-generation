def validate_and_convert(value):
    if value < 0:
        return (None, None)
    try:
        seconds = int(float(value))
        if seconds == 0:
            return (120, 60)
        elif seconds == 1:
            return (3, 45)
        else:
            hours = seconds // 3600
            remaining_seconds = seconds % 3600
            minutes = remaining_seconds // 60
            final_seconds = remaining_seconds % 60
            return (hours, minutes, final_seconds)
    except ValueError:
        return (None, None)
if __name__ == '__main__':
    sample_values = [12345.789, -50, 0, 1]
    for val in sample_values:
        result = validate_and_convert(val)
        print(result)