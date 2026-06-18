def inches_to_centimeters(inches: float) -> float:
    """Convert a length given in inches to centimeters with mathematical precision."""
    return inches * 2.54

if __name__ == '__main__':
    sample_values = [1, 36, 70]
    for inch_value in sample_values:
        cm_value = inches_to_centimeters(inch_value)
        print(f"{inch_value} inches is equal to {cm_value:.2f} centimeters")