def convert_duration(duration, unit):
    conversions = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }
    unit = unit.lower()
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if duration < 0:
        raise ValueError("Duration cannot be negative")
    base_seconds = duration * conversions[unit]
    return {
        "seconds": base_seconds,
        "minutes": base_seconds / 60,
        "hours": base_seconds / 3600,
        "days": base_seconds / 86400
    }

if __name__ == '__main__':
    result = convert_duration(1440, "minutes")
    print(result)