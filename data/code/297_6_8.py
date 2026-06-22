SECONDS_PER_HOUR = 3600
MILLISECONDS_PER_SECOND = 1000

def validate_hours(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        raise ValueError("Hours must be a non-negative number")

def hours_to_milliseconds(hours):
    validate_hours(hours)
    return int(hours * SECONDS_PER_HOUR * MILLISECONDS_PER_SECOND)

if __name__ == '__main__':
    print(hours_to_milliseconds(2))
    print(hours_to_milliseconds(5))