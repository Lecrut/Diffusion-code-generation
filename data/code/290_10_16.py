def convert_mass(grams):
    return grams / 28.3495

if __name__ == '__main__':
    mass_grams = 2500
    result_ounces = convert_mass(mass_grams)
    print(f"Input Mass: {mass_grams} g")
    print(f"Converted Mass: {result_ounces} oz")