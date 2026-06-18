def inches_to_cm(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision."""
    return inches * 2.54

if __name__ == '__main__':
    sample_values = [1, 36, 70]
    for inch_val in sample_values:
        cm_val = inches_to_cm(inch_val)
        print(f"{inch_val} inches is exactly {cm_val:.2f} centimeters")