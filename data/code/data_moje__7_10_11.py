def convert_duration(value, unit):
    seconds = 0.0
    if unit == "seconds":
        seconds = float(value)
    elif unit == "minutes":
        seconds = float(value) * 60
    elif unit == "hours":
        seconds = float(value) * 3600
    elif unit == "days":
        seconds = float(value) * 86400
    else:
        raise ValueError("Unsupported unit: {}. Use 'seconds', 'minutes', 'hours', or 'days'.".format(unit))
    
    days = seconds / 86400
    hours = (seconds % 86400) / 3600
    minutes = (seconds % 3600) / 60
    secs = seconds % 60
    
    return {
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days
    }

if __name__ == '__main__':
    result = convert_duration(1.5, "days")
    print(result)