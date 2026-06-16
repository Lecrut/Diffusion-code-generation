def bidirectional_conversion(value, unit):
    if unit == "meters":
        if value >= 0:
            return value * 0.000621371
        else:
            return value * 0.000621371
    elif unit == "miles":
        if value >= 0:
            return value / 0.000621371
        else:
            return value / 0.000621371
    else:
        raise ValueError("Invalid unit specified. Use 'meters' or 'miles'.")
if __name__ == '__main__':
    sample_value = 10
    sample_unit = "meters"
    meters_to_miles = bidirectional_conversion(sample_value, sample_unit)
    miles_to_meters = bidirectional_conversion(meters_to_miles, "miles")
    print(f"Original value: {sample_value} {sample_unit}")
    print(f"Conversion to miles: {meters_to_miles}")
    print(f"Conversion back to meters: {miles_to_meters}")
    sample_value = 5
    sample_unit = "miles"
    meters_to_miles = bidirectional_conversion(sample_value, sample_unit)
    miles_to_meters = bidirectional_conversion(meters_to_miles, "meters")
    print(f"\nOriginal value: {sample_value} {sample_unit}")
    print(f"Conversion to meters: {meters_to_miles}")
    print(f"Conversion back to miles: {miles_to_meters}")