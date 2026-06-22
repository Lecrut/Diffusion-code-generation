def convert_duration(value, unit):
    valid_units = ["seconds", "minutes", "hours", "days"]
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Value must be a non-negative number")

    if unit == "seconds":
        total_seconds = value
    elif unit == "minutes":
        total_seconds = value * 60
    elif unit == "hours":
        total_seconds = value * 3600
    elif unit == "days":
        total_seconds = value * 86400

    seconds = total_seconds
    minutes = total_seconds / 60
    hours = total_seconds / 3600
    days = total_seconds / 86400

    return {
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days
    }

class DurationConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.conversions = convert_duration(value, unit)

    def get_all_conversions(self):
        return self.conversions

    def get_unit(self, target_unit):
        valid_units = ["seconds", "minutes", "hours", "days"]
        if target_unit not in valid_units:
            raise ValueError(f"Invalid target unit: {target_unit}")
        return self.conversions[target_unit]

if __name__ == '__main__':
    sample_data = [
        (1, "minutes"),
        (2.5, "hours"),
        (3, "days"),
        (60, "seconds")
    ]

    for val, unit in sample_data:
        converter = DurationConverter(val, unit)
        result = converter.get_all_conversions()
        print(f"Original: {val} {unit}")
        print(f"Converted: {result}")
        print(f"Specific Minutes: {converter.get_unit('minutes')}")
        print("---")