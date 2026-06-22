def calculate_equivalent_weight(mass):
    molar_mass = 74.09
    oxygen_mass = 16 * 2
    if mass <= 0:
        raise ValueError("Mass must be greater than zero")
    if molar_mass <= oxygen_mass:
        raise ValueError("Molar mass must be greater than the total oxygen mass")
    equivalent_weight = mass / (molar_mass - oxygen_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 74
    result = calculate_equivalent_weight(sample_mass)
    print(result)