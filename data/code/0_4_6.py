def inches_to_centimeters(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision."""
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = [1, 12, 36]
    for inch_value in sample_inches:
        cm_value = inches_to_centimeters(inch_value)
        print(f"{inch_value} inches is exactly {cm_value} centimeters")