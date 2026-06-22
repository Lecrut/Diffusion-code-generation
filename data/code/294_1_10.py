def calculate_water_equivalent_weight(mass):
    molar_mass = 18.015
    return mass / molar_mass

if __name__ == '__main__':
    sample_mass = 18
    print(calculate_water_equivalent_weight(sample_mass))