def convert_grams_to_ounces(grams):
    conversion_factor = 28.3495
    ounces = grams / conversion_factor
    return float(ounces)

if __name__ == '__main__':
    sample_mass_g = 7000
    result_oz = convert_grams_to_ounces(sample_mass_g)
    print(f"Input Mass: {sample_mass_g} g")
    print(f"Converted Mass: {result_oz:.2f} oz")