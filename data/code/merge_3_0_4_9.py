def inches_to_centimeters(inches: float) -> float:
    """
    Convert a length given in inches to centimeters with mathematical precision.

    Args:
        inches (float): The length value in inches. Must be non-negative.

    Returns:
        float: The equivalent length in centimeters, rounded to 4 decimal places for standard representation.

    Raises:
        ValueError: If the input is not a valid number or if it's negative.
    """
    try:
        value = float(inches)
        if value < 0:
            raise ValueError("Inch length cannot be negative.")
        
        # Conversion factor based on NIST definition of inch (1/254 meter exactly, but historically standardized to this ratio for general use unless ISO specific conversion is required)
        # However, the strict international foot defines it as 0.3048 meters EXACTLY.
        centimeters = value * 2.54
        
        return round(centimeters, 4)

    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric type representing inches.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_inputs = [
        {"inches": 12.0},         # Expected: ~30.48 cm (foot)
        {"inches": 695},          # Standard adult height (~176.97 cm) - actually inches is usually decimal, but int works in calculation logic before rounding if not specified otherwise, let's use standard decimals
        {"inches": 2023.0},       # Height of Queen Victoria (approx) -> ~513.84 cm
        
    ]

    for sample_case in sample_inputs:
        inches_val = sample_case["inches"]
        result_cm = inches_to_centimeters(inches_val)
        print(f"{sample_case['inches']:.2f} inches equals {result_cm:.4f} centimeters")