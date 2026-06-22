def grams_to_ounces(grams):
    conversion_factor = 28.3495
    ounces = grams / conversion_factor
    return float(ounces)

if __name__ == '__main__':
    mass_g = 1000
    result = grams_to_ounces(mass_g)
    print(f"Input Mass: {mass_g} g")
    print(f"Converted Mass: {result} oz")