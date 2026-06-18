import sys

def convert_length(value: float, unit_str: str) -> tuple[float, float]:
    """
    Convert a length value from the specified input unit to meters and feet.
    
    Supported units (case-insensitive): 'km', 'm'.
    Returns a tuple of (value_in_meters, value_in_feet).
    
    Args:
        value: The numerical length value.
        unit_str: String representing the source unit ('km' or 'm').
        
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be a number, got {type(value).__name__}")

    # Define conversion factors relative to meters
    km_to_m = 1000.0
    m_to_m = 1.0
    
    unit_lower = unit_str.lower().strip() if isinstance(unit_str, str) else ""
    
    try:
        factor = float(km_to_m) if unit_lower == "km" else (float(m_to_m) if unit_lower == "m" else None)
        
        if factor is not None and value != 0.0 or unit_lower in ("km", "m"):
            meters = value * factor
            
            # Convert meters to feet: 1 meter ≈ 3.28084 feet
            feet = meters * 3.28084
            
            return meters, feet
        else:
            raise ValueError("Unsupported unit provided.")
            
    except (ValueError, TypeError):
        raise ValueError(f"Invalid conversion factor for unit '{unit_str}'.")

def format_output(value_meters: float, value_feet: float) -> str:
    """Format the converted values into a readable string."""
    return f"{value_meters:.2f} meters and {value_feet:.2f} feet"

if __name__ == '__main__':
    # Hard-coded sample data for demonstration purposes.
    # Format expected by input: "unit value" (e.g., 'km 5', 'm 10')
    
    raw_data = [
        ("km", 2),      # Example: 2 kilometers
        ("m", 3456),    # Example: 3,456 meters
        ("miles", None) # Note: miles is not supported per task requirements (only km/m specified in prompt logic above). 
                        # To strictly adhere to the "specified unit" instruction which mentioned kilometers as an example but allowed 'e.g.', 
                        # we will stick to KM and M only. If a user passes miles, it raises ValueError.
    ]

    print("Converting lengths...")
    
    for item in raw_data:
        if len(item) != 2 or not isinstance(item[1], (int, float)):
            continue
            
        unit_str = str(item[0])
        value = item[1]
        
        try:
            meters, feet = convert_length(value, unit_str)
            print(format_output(meters, feet))
        except ValueError as e:
            if "Unsupported" in str(e):
                print(f"Error for {unit_str}: {e}")