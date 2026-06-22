conversion_factors = {
    'g': 1 / 28.3495,
}

def convert_mass(value):
    return value * conversion_factors['g']

if __name__ == '__main__':
    mass_g = 2500
    result_oz = convert_mass(mass_g)
    print(f"Input Mass: {mass_g} g")
    print(f"Converted Mass: {result_oz} oz")