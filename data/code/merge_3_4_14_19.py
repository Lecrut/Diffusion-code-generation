import argparse

def convert_distance(distance_value: float, from_unit: str, to_unit: str) -> tuple[float | None]:
    """Converts a distance value between metric units (km, m, cm)."""
    
    # Define conversion factors relative to kilometers
    unit_factors = {
        'km': 1.0,
        'm': 0.001,
        'cm': 0.00001
    }

    factor_from = unit_factors.get(from_unit.lower())
    if not factor_from:
        return None
    
    # Convert input to kilometers first for intermediate calculation
    distance_km = distance_value * factor_from

    target_factor = unit_factors.get(to_unit.lower())
    if not target_factor:
        return None

    result = distance_km / target_factor
    return round(result, 6)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments
    
    sample_distance = 50.0
    from_unit_str = 'km'
    to_unit_str = 'm'

    try:
        result_value = convert_distance(sample_distance, from_unit_str, to_unit_str)
        
        if result_value is None:
            print(f"Error: Invalid unit provided.")
            print(f"Accepted units are: km, m, cm")
        else:
            print(f"{sample_distance} {from_unit_str} = {result_value} {to_unit_str}")

    except Exception as e:
        # Fallback for unexpected errors during conversion logic (e.g., float parsing if changed)
        error_msg = f"An internal calculation error occurred. Details: {str(e)}"
        print(error_msg)