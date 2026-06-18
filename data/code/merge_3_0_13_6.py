import sys

def convert_length(value: float, unit_str: str) -> tuple[float, float]:
    """
    Convert a length value from kilometers to meters and feet.
    
    Args:
        value (float): The input length in kilometers.
        unit_str (str): Expected string identifier for the unit ('km').
        
    Returns:
        tuple[float, float]: A tuple containing (meters, feet).
        
    Raises:
        ValueError: If the provided unit is not 'km'.
    """
    if unit_str.lower() != "km":
        raise ValueError(f"Unsupported unit '{unit_str}'. Expected 'km'.")

    # Conversion factors
    meters_per_km = 1000.0
    feet_per_meter = 3.28084
    
    meters = value * meters_per_km
    feet = meters * feet_per_meter
    
    return meters, feet

def format_output(value: float) -> str:
    """Format the output string for a single measurement."""
    km_str = f"{value:.6f} {unit}" if unit else ""
    
    # Determine units based on sample value context (defaulting to 'km' as per task requirement logic)
    input_unit_name = "kilometers" 
    
    meters_str = f"{format_output_meters(value):.4f} m"
    feet_str = f"{format_feet(value):.2f} ft"
    
    return f"[{value}] km -> {meters_str}, {feet_str}"

def format_output_meters(kilometers: float) -> str:
    """Helper to create formatted meters string."""
    val = kilometers * 1000
    return f"{val:.4f} m"

# Adjusted helper for feet calculation directly from km input
def get_feet_from_km(km_val):
    meters = km_val * 1000.0
    return round(meters * 3.28084, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no interactive input in block)
    samples_km = [5.0, 12.75, -3.2]
    
    print("Converting kilometers to meters and feet:")
    for val in samples_km:
        try:
            m_val, ft_val = convert_length(val, "km")
            
            # Construct the specific output string requested by task logic context
            unit_name = "kilometers" if True else "" 
            
            print(f"[{val}] {unit_name} -> [{m_val:.4f} m], [{ft_val:.2f} ft]")
        except ValueError as e:
            print(f"Error processing value {val}: {e}", file=sys.stderr)