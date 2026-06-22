def calculate_equivalent_weight(mass_of_water):
    molar_mass_h2o = 18.015
    atomic_mass_oxygen = 16
    number_of_oxygens_per_molecule = 2
    equivalent_weight = (mass_of_water / molar_mass_h2o) * atomic_mass_oxygen * number_of_oxygens_per_molecule
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 18
    result = calculate_equivalent_weight(sample_mass)
    print(result)