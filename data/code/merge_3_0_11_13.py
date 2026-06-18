def convert_length(value: float, unit_type: str) -> float:
    """
    Converts a length value from meters to feet or vice versa.
    
    Args:
        value (float): The numerical length value.
        unit_type (str): The source unit type ('m' for meters, 'ft' for feet).
        
    Returns:
        float: The converted length in the opposite unit system.
    """
    if unit_type == "m":
        # 1 meter = approximately 3.28084 feet
        return value * 3.28084
    elif unit_type == "ft":
        # 1 foot = approximately 0.3048 meters (or divide by 3.28084)
        return value / 3.28084
    else:
        raise ValueError("Unsupported unit type. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    # Sample conversions without interactive input
    sample_meters = [1, 5, 10]
    sample_feet = [3, 10, 20]

    print("Converting meters to feet:")
    for val in sample_meters:
        converted_ft = convert_length(val, "m")
        print(f"{val} m -> {converted_ft:.4f} ft")

    print("\nConverting feet to meters:")
    for val in sample_feet:
        converted_m = convert_length(val, "ft")
        print(f"{val} ft -> {converted_m:.4f} m")