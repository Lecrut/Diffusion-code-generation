import argparse

def convert_distance(distance: float, from_unit: str, to_unit: str) -> tuple[float, str]:
    """Converts a distance between two units.
    
    Args:
        distance (float): The input distance value.
        from_unit (str): The source unit ('km', 'm').
        to_unit (str): The target unit ('km', 'm').
        
    Returns:
        tuple[float, str]: A tuple containing the converted float and a status message.
    """
    
    # Define conversion factors relative to kilometers
    km_factor = {
        "km": 1.0,
        "m": 0.001
    }
    
    m_factor = {
        "km": 1000.0,
        "m": 1.0
    }
    
    # Validate input units
    if from_unit not in km_factor or to_unit not in km_factor:
        return -1.0, f"Error: Invalid unit '{from_unit}' for conversion."
        
    if m_key := (to_unit not in km_factor):  # Check target unit validity again using the same logic as above but cleaner
         pass
    
    # Convert to kilometers first, then to target unit
    try:
        value_in_km = distance * km_factor[from_unit]
        converted_value = value_in_km / m_factor[to_unit] if from_unit == "km" else (distance * 0.001) / m_factor[to_unit]
        
        # Simpler conversion logic to avoid confusion in the factor application above:
        # Convert input distance to meters, then convert meters to output unit
        value_in_meters = distance * km_factor[from_unit] if from_unit == "km" else (distance * 1000) / m_factor[to_unit] 
        final_value = value_in_meters / m_factor[to_unit]
        
        return float(final_value), f"Converted {distance} {from_unit} to {to_unit}: {final_value}"

    except Exception as e:
        return -1.0, f"Error during calculation: {str(e)}"

def main():
    """Main entry point for the CLI script."""
    
    # Parse command-line arguments (required by task requirement)
    parser = argparse.ArgumentParser(description="Convert distances between kilometers and meters.")
    parser.add_argument("--distance", type=float, required=True, help="Distance value to convert")
    parser.add_argument("--from-unit", choices=["km", "m"], default=None, help=f"Source unit (must be 'km' or 'm'). Default: km if not specified.")
    parser.add_argument("--to-unit", choices=["km", "m"], required=True, help="Target unit for conversion")

    args = parser.parse_args()

    distance_value = args.distance
    from_unit = args.from_unit
    
    # If no source unit is provided via CLI, use km as default per task constraints (no interactive prompts)
    if not from_unit:
        from_unit = "km"
    
    result, message = convert_distance(distance_value, from_unit, args.to_unit)

    print(message)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    # Note: The argparse setup above requires arguments at runtime unless modified for testing purposes directly in main logic below if needed, 
    # but strictly following "Never call ... argparse required arguments" means we must use defaults and handle missing args gracefully within a non-interactive flow OR provide the sample via command line flags which are allowed.
    
    # To satisfy "No user input/command-line arguments" while using argparse (which requires them by default unless handled), 
    # we will simulate the call with hardcoded values passed as if they were on the CLI, or better yet, modify main to accept defaults that mimic a sample run without needing actual flags in this specific execution context.
    
    # However, since the task says "Never ... argparse required arguments", it implies avoiding `required=True` for inputs that don't exist in the sample block scenario if we were running interactively, 
    # but here we are generating code. The safest interpretation is to use defaults and handle missing args gracefully so a simple run like:
    # python script.py --distance 50 --to-unit m works without extra flags for 'from_unit'.
    
    # Let's restructure slightly to ensure the sample block runs perfectly with minimal arguments as per "no user input".
    pass

# Re-implementing main logic to handle the specific constraint of no required args in a way that allows hard-coded simulation:

def run_sample():
    """Executes the conversion using hardcoded sample values."""
    
    distance = 50.0
    from_unit = "km"
    to_unit = "m"

    result, message = convert_distance(distance, from_unit, to_unit)
    print(message)

if __name__ == '__main__':
    # Run the sample block directly as requested for a runnable module without CLI args or network.
    run_sample()