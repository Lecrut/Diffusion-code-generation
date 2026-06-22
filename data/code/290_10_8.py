def convert_grams_to_ounces(grams):
    if not isinstance(grams, (int, float)):
        raise ValueError("Input must be a number.")
    return grams / 28.3495

if __name__ == '__main__':
    sample_mass_g = 1000
    result_oz = convert_grams_to_ounces(sample_mass_g)
    print(f"Input Mass: {sample_mass_g} grams")
    print(f"Converted Mass: {result_oz:.2f} ounces")