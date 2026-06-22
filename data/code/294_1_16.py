def calculate_equivalent_weight(mass_of_water):
    molar_mass_of_water = 18.015
    atomic_mass_of_oxygen = 16
    return mass_of_water / (atomic_mass_of_oxygen * 2 + 1)

if __name__ == '__main__':
    sample_mass = 18
    print(calculate_equivalent_weight(sample_mass))