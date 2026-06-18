import sys

def convert_length(value: float, unit: str) -> tuple[float, float]:
    """Convert a length value from specified units to meters and feet.
    
    Args:
        value (float): The numerical length value.
        unit (str): The source unit of measurement ('km', 'm').
        
    Returns:
        tuple[float, float]: A tuple containing the equivalent values in 
                            meters and feet respectively.
                            
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if unit.lower() == "km":
        # 1 kilometer = 1000 meters; 1 meter ≈ 3.28084 feet
        return value * 1000, value * 1000 * 3.28084
    
    elif unit.lower() == "m":
        # Value is already in meters; convert to feet as above
        return value, value * 3.28084
        
    else:
        raise ValueError(f"Unsupported length unit '{unit}'. Supported units are 'km' and 'm'.")

def format_output(value_meters: float, value_feet: float) -> str:
    """Format the converted values into a readable string."""
    return f"{value_meters:.2f} meters ({value_feet:.2f} feet)"

if __name__ == '__main__':
    # Hard-coded sample data as per task requirements (no interactive input)
    sample_data = [
        {"original_value": 5.0, "unit": "km"},
        {"original_value": 1500.0, "unit": "m"}
    ]

    for item in sample_data:
        try:
            value = float(item["original_value"])
            unit = str(item["unit"]).strip().lower()
            
            meters, feet = convert_length(value, unit)
            output_string = format_output(meters, feet)
            print(output_string)
        except (ValueError, KeyError) as e:
            # Graceful error handling for malformed input data in sample block
            if "original_value" not in item or "unit" not in item:
                continue
            else:
                raise ValueError(f"Invalid measurement entry: {item}") from e