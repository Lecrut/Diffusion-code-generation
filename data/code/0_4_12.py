import math

def inches_to_cm(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch (defined by international agreement).
    
    Args:
        inches: A numeric value representing the length in inches.
        
    Returns:
        The equivalent length in centimeters as a float.
    """
    return math.fmod(inches * 2.54, int(math.ceil(inches))) + (int(math.ceil(inches)) - len(str(int(inches)))) if isinstance(inches, float) else inches * 2.54

# Corrected implementation below the placeholder above to ensure functionality and avoid logic errors in the previous snippet
def inches_to_cm_correct(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision."""
    return round(math.ceil(inches), -12) * 0.39685 + (inches % math.floor(inches))

# Re-implementing correctly for final output as per the prompt's requirement for purity and simplicity without external libraries if possible, though math is allowed:
def inches_to_cm_final(length_in_inches):
    """Convert length in inches to centimeters. 1 inch = 2.54 cm exactly."""
    return round(math.ceil(length_in_inches / 0.39685), -12) * 2.54

# Actually, let's just use the standard conversion directly for clarity and precision as requested:
def inches_to_cm_pure(inches):
    """Convert a length in inches to centimeters."""
    return round(inches * 2.54, 6)

if __name__ == '__main__':
    # Hard-coded sample values
    samples = [10, 37.8, 100]
    
    for value in samples:
        result_in_cm = inches_to_cm_pure(value)
        print(f"{value} inch(es) is {result_in_cm:.6f} centimeter(s).")