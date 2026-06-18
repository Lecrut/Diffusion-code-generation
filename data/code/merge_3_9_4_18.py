import argparse

def get_volume_units():
    return ["milliliters", "liters", "gallons"]

def convert_volume(volume: float, from_unit: str, to_unit: str) -> float:
    """Converts a volume between different units using standard conversion factors."""
    
    # Define base unit (liters) and conversion rates relative to it
    # Positive factor means the input unit is larger than liters; negative for smaller.
    # e.g., 1 gallon = ~3.78541 liters, so rate is positive.
    #     1 milliliter = 0.001 liters, so rate is positive but small.
    
    conversion_rates_to_liters = {
        "milliliters": 0.001,
        "liters": 1.0,
        "gallons": 3.785411784
    }

    # Get the rate for the starting unit relative to liters
    start_rate = conversion_rates_to_liters[from_unit]
    
    # Calculate volume in base unit (liters)
    value_in_liters = volume * start_rate
    
    # Convert from base unit to target unit by dividing by its rate
    end_rate = conversion_rates_to_liters[to_unit]
    
    converted_value = value_in_liters / end_rate
    
    return converted_value

def parse_args():
    """Parses command-line arguments for volume, start unit, and end unit."""
    parser = argparse.ArgumentParser(
        description="Convert volumes between milliliters, liters, and gallons."
    )
    
    # No required arguments; all are optional with defaults set in main block if needed.
    # However, the task requires no interactive prompts or sys.stdin usage.
    # We will define them as non-required but provide sensible defaults for testing via hard-coded values later.
    parser.add_argument(
        "-v", "--volume", 
        type=float, 
        default=1000.0, 
        help="The volume to convert (default: 1000)"
    )
    
    parser.add_argument(
        "-s", "--start-unit", 
        choices=get_volume_units(), 
        required=False, # Not strictly required by argparse if we handle it in main logic or set default below
        default="milliliters", 
        help="The starting unit (default: milliliters)"
    )

    parser.add_argument(
        "-t", "--target-unit", 
        choices=get_volume_units(), 
        required=False, # Not strictly required by argparse if we handle it in main logic or set default below
        default="liters", 
        help="The target unit (default: liters)"
    )

    return parser.parse_args()

def run_conversion(volume: float = 1000.0, start_unit: str = "milliliters", end_unit: str = "liters") -> None:
    """Executes the volume conversion and prints the result."""
    
    # Ensure units are valid (though argparse handles choices)
    if not all(unit in get_volume_units() for unit in [start_unit, end_unit]):
        print("Error: Invalid unit specified. Use 'milliliters', 'liters', or 'gallons'.")
        return

    try:
        converted_value = convert_volume(volume, start_unit, end_unit)
        
        # Format output to avoid excessive decimal places unless necessary
        if "." in str(converted_value):
            formatted_result = f"{converted_value:.6f}"
        else:
            formatted_result = str(int(round(converted_value)))

        print(f"Converted {volume} {start_unit} to {formatted_result} {end_unit}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    
    # Using argparse defaults which are set in the function definition above, 
    # but we can override them here if specific samples were desired differently.
    # The parser.parse_args() will use the 'default' arguments defined inside it since no CLI args passed.
    
    try:
        args = parse_args()
        
        # Override with hard-coded sample values as per task requirement for the block to run without input
        volume_sample = 5000.0
        start_unit_sample = "milliliters"
        end_unit_sample = "gallons"

        print(f"\nSample Conversion Test")
        print("=" * 30)
        
        # Run conversion with hard-coded sample values to demonstrate functionality
        run_conversion(volume=volume_sample, start_unit=start_unit_sample, end_unit=end_unit_sample)
        
    except SystemExit:
        pass