def validate_mass(mass):
    if not isinstance(mass, (int, float)):
        raise ValueError("Invalid mass. Must be a number.")
    if mass < 0:
        raise ValueError("Mass cannot be negative.")

def convert_grams_to_ounces(grams):
    return grams / 28.3495

if __name__ == '__main__':
    sample_mass_g = 100
    validate_mass(sample_mass_g)
    result_oz = convert_grams_to_ounces(sample_mass_g)
    print(f"Input Mass: {sample_mass_g} g")
    print(f"Converted Mass: {result_oz} oz")