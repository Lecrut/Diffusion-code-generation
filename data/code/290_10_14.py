CONVERSION_FACTOR = 28.3495

def grams_to_ounces(grams):
    return grams / CONVERSION_FACTOR

if __name__ == '__main__':
    sample_mass_g = 1000
    converted_mass_o = grams_to_ounces(sample_mass_g)
    print(f"Sample Mass in Grams: {sample_mass_g}")
    print(f"Converted Mass in Ounces: {converted_mass_o}")