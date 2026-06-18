def inches_to_cm(inches: float) -> float:
    """
    Converts a length given in inches to centimeters with mathematical precision.
    
    Args:
        inches (float): The length value in inches. Must be non-negative.
        
    Returns:
        float: The equivalent length in centimeters, rounded to the nearest integer 
              if necessary based on floating-point representation for display purposes.
              However, internally uses exact multiplication by 2.54.

    Note:
        One inch is exactly defined as 0.0254 meters or 2.54 centimeters.
        The conversion formula is: cm = inches * 2.54
    """
    if inches < 0:
        raise ValueError("Input length cannot be negative.")
    
    # Using the exact definition of an inch in terms of centimeters
    return round(inches * 2.54, 1)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [36, 70, 18, 29]

    for inch_val in samples:
        cm_val = inches_to_cm(inch_val)
        print(f"{inch_val} inches is {cm_val} centimeters")