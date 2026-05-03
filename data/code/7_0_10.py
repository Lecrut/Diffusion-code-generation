def convert_time(time_value, source_unit, target_unit):
    if source_unit == target_unit:
        return time_value
    seconds = 0
    if source_unit == "seconds":
        seconds = time_value
    elif source_unit == "minutes":
        seconds = time_value * 60
    elif source_unit == "hours":
        seconds = time_value * 3600
    else:
        raise ValueError("Invalid source unit")
    if target_unit == "seconds":
        return seconds
    elif target_unit == "minutes":
        return seconds / 60
    elif target_unit == "hours":
        return seconds / 3600
    else:
        raise ValueError("Invalid target unit")
if __name__ == '__main__':
    print(convert_time(3600, "seconds", "minutes"))
    print(convert_time(120, "minutes", "hours"))
    print(convert_time(3600, "hours", "seconds"))
    print(convert_time(7200, "seconds", "hours"))
    print(convert_time(90, "minutes", "seconds"))
    print(convert_time(180, "hours", "minutes"))