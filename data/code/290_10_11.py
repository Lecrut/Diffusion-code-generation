def convert_grams_to_ounces(grams):
    conversion_factor = 1 / 28.3495
    return grams * conversion_factor

if __name__ == '__main__':
    mass_g = 2500
    result_oz = convert_grams_to_ounces(mass_g)
    print(f"Input Mass: {mass_g} g")
    print(f"Converted Mass: {result_oz} oz")