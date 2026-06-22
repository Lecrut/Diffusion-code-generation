def validate_conversion_factor(factor):
    if not isinstance(factor, (int, float)) or factor <= 0:
        raise ValueError("Conversion factor must be a positive number")

def convert_liters_to_gallons(liters):
    liters_per_gallon = 3.78541
    conversion_factor = 1 / liters_per_gallon
    validate_conversion_factor(conversion_factor)
    return conversion_factor

if __name__ == '__main__':
    sample_liters = 10
    factor = convert_liters_to_gallons(sample_liters)
    print(f"Conversion factor for {sample_liters} liters to gallons: {factor:.4f}")