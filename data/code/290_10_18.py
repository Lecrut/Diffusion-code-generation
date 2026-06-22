CONVERSION_FACTOR = 28.3495

def convert_grams_to_ounces(grams):
    return grams / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_mass_g = 1000
    result_oz = convert_grams_to_ounces(sample_mass_g)
    print(f"Input Mass: {sample_mass_g} g")
    print(f"Converted Mass: {result_oz} oz")