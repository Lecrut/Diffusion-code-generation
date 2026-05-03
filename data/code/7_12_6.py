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
    print(convert_time(3600, "seconds", "minutes"))
    print(convert_time(120, "minutes", "hours"))
    print(convert_time(86400, "hours", "days"))
    print(convert_time(1, "days", "hours"))
    print(convert_time(5000, "milliseconds", "seconds"))
    print(convert_time(1000000, "microseconds", "seconds"))
    print(convert_time(7200, "seconds", "days"))
    try:
        convert_time(10, "seconds", "furlongs")
    except ValueError as e:
        print(f"Error caught: {e}")