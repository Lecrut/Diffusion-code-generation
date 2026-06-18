import argparse
from typing import Optional

# Conversion factors to metric base (grams)
CONVERSION_FACTORS = {
    "kg": 1000,        # Kilograms -> Grams
    "g": 1,            # Grams -> Grams
    "mg": 1e-3,        # Milligrams -> Grams
    "oz": 28.349523125, # Ounces (avoirdupois) -> Grams
    "lb": 453.59237,   # Pounds -> Grams
}

# Reverse conversion factors to output unit (grams per source unit)
SOURCE_TO_METRIC = CONVERSION_FACTORS.copy()

def get_conversion_factor(source_unit: str, target_unit: str) -> float:
    """Calculate the direct conversion factor from source unit to target unit."""
    metric_value_per_source = SOURCE_TO_METRIC.get(
        source_unit.lower(), None
    )
    
    if metric_value_per_source is None:
        raise ValueError(f"Unsupported input unit: {source_unit}")

    # Target value per 1 gram of output (since we are normalizing to grams)
    target_metric_factor = SOURCE_TO_METRIC.get(
        target_unit.lower(), None
    )
    
    if target_metric_factor is None:
        raise ValueError(f"Unsupported output unit: {target_unit}")

    # Conversion logic: Value * Factor_to_Grams / Factor_from_Output_Gram_per_1_Unit (which is just the factor itself)
    return metric_value_per_source / target_metric_factor

def convert_volume(value_as_string: str, input_unit: str, output_unit: str) -> tuple[float, float]:
    """Convert a value from one unit to another."""
    
    # Parse numeric value with basic error handling for non-numeric inputs
    try:
        value = float(value_as_string.strip()) if isinstance(value_as_string, str) else value_as_string
    except ValueError as e:
        raise ValueError(f"Invalid input volume. Must be a valid number.") from e
    
    # Validate units exist in the conversion table
    unit_lower_input = input_unit.lower()
    unit_lower_output = output_unit.lower()

    if unit_lower_input not in SOURCE_TO_METRIC or \
       unit_lower_output not in CONVERSION_FACTORS:
        raise ValueError(f"Invalid unit specified. Supported units are 'kg', 'g', 'mg', 'oz', 'lb'")

    # Perform the conversion using pre-calculated factors for robustness and speed
    factor = get_conversion_factor(unit_lower_input, unit_lower_output)
    
    converted_value: float = value * factor
    
    return converted_value, factor

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert volume units between metric and imperial systems.")

    # Define non-interactive arguments with default values
    group_volume_unit = parser.add_mutually_exclusive_group()  # Not using required to avoid blocking prompts
    
    def setup_input_units(group):
        """Helper to add mutually exclusive unit choices."""
        
        for key, val in CONVERSION_FACTORS.items():
            group.add_argument(f"--from-{key}", action="store", default=None)

    
    parser.add_argument("--value-from-kg", type=float, help="Input value if using kilograms")
    parser.add_argument("--unit-to-g", choices=["g", "mg"], dest="input_unit_target_metric", nargs=1, const='g', metavar=("UNIT"), action='append')  # Using append with constant to simulate choice logic without required args
    
    # Simulating the selection process by defaulting based on flags present or using defaults
    input_value = 5.0
    input_unit_default = "kg" 
    output_unit_default = "g"

    parsed_args: Optional[argparse.Namespace] = parser.parse_args()
    
    if not hasattr(parsed_args, 'input_unit_target_metric'):
        # Fallback to defaults for the sample run as requested (no user interaction)
        input_value = 5.0
        input_unit_default = "kg" 
        output_unit_default = "g"

    # Force execution with hardcoded values per requirement
    final_input_value = float(input_value)
    final_output_unit = output_unit_default if 'output_unit' not in dir(parsed_args, parsed_args.__dict__) else getattr(parsed_args, 'unit_to_g', None)[0] or output_unit_default
    
    print(f"Converting {final_input_value} from {input_unit_default} to {final_output_unit}")

    try:
        converted_result = convert_volume(final_input_value, input_unit_default, final_output_unit)
        
        # Extract the actual value and factor for clarity if needed, but primarily return the result string
        
        print(f"Converted Value: {converted_result:.6f} units of {final_output_unit}")

    except ValueError as ve:
        print(f"Error: {ve}", file=__import__('sys').stderr)
        
# Final hardcoded sample run logic is embedded in the `if __name__ == '__main__':` block above.