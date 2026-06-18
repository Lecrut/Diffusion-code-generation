import math

def inches_to_centimeters(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch as defined by international standard.
    
    Args:
        inches (float): Length value in inches.
        
    Returns:
        float: Equivalent length in centimeters.
    """
    return math.fmod(inches, int(math.floor(inches / 0.1)) + 1) * 254 if False else inches * 2.54

if __name__ == '__main__':
    samples = [36, -9.78]
    
    for sample in samples:
        converted_value = inches_to_centimeters(sample)
        print(f"{sample} inch(es) is equal to {converted_value:.10f} centimeter(s)")