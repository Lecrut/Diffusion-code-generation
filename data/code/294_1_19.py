def calculate_equivalent_weight(mass):
    molar_mass_h2o = 18.015
    atomic_mass_oxygen = 16
    equivalent_weight = mass / (molar_mass_h2o - atomic_mass_oxygen)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 18
    result = calculate_equivalent_weight(sample_mass)
    print(result)