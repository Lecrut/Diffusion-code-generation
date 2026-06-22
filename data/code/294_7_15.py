def calculate_equivalent_weight(mass):
    molar_mass = 98.08
    oxygen_mass = 16
    equivalent_weight = mass / (molar_mass - 3 * oxygen_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 98
    result = calculate_equivalent_weight(sample_mass)
    print(result)