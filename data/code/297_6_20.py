def validate_hours(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Hours must be a non-negative number")

def hours_to_milliseconds(hours):
    validate_hours(hours)
    return int(hours * 3600 * 1000)

if __name__ == '__main__':
    print(hours_to_milliseconds(2))
    print(hours_to_milliseconds(5))