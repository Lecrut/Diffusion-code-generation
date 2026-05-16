def convert_time(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    seconds = 0
    if from_unit == "seconds":
        seconds = value
    elif from_unit == "minutes":
        seconds = value * 60
    elif from_unit == "hours":
        seconds = value * 3600
    elif from_unit == "days":
        seconds = value * 86400
    elif from_unit == "weeks":
        seconds = value * 604800
    elif from_unit == "milliseconds":
        seconds = value / 1000.0
    elif from_unit == "microseconds":
        seconds = value / 1000000.0
    else:
        raise ValueError("Unsupported 'from_unit'")
    if to_unit == "seconds":
        return seconds
    elif to_unit == "minutes":
        return seconds / 60.0
    elif to_unit == "hours":
        return seconds / 3600.0
    elif to_unit == "days":
        return seconds / 86400.0
    elif to_unit == "weeks":
        return seconds / 604800.0
    elif to_unit == "milliseconds":
        return seconds * 1000.0
    elif to_unit == "microseconds":
        return seconds * 1000000.0
    else:
        raise ValueError("Unsupported 'to_unit'")
if __name__ == '__main__':
    print(f"1 hour to minutes: {convert_time(3600, 'hours', 'minutes')}")
    print(f"60 minutes to seconds: {convert_time(60, 'minutes', 'seconds')}")
    print(f"3600 seconds to hours: {convert_time(3600, 'seconds', 'hours')}")
    print(f"24 hours to days: {convert_time(24, 'hours', 'days')}")
    print(f"1 day to seconds: {convert_time(1, 'days', 'seconds')}")
    print(f"1000 milliseconds to seconds: {convert_time(1000, 'milliseconds', 'seconds')}")
    print(f"1000 seconds to milliseconds: {convert_time(1000, 'seconds', 'milliseconds')}")
    print(f"1000000 microseconds to seconds: {convert_time(1000000, 'microseconds', 'seconds')}")
    print(f"1 week to hours: {convert_time(1, 'weeks', 'hours')}")
    try:
        convert_time(10, 'years', 'days')
    except ValueError as e:
        print(f"Error caught: {e}")