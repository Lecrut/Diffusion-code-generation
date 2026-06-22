def calculate_co2_equivalent_weight(mass):
    molar_mass = 44.01
    return mass / molar_mass

if __name__ == '__main__':
    sample_mass = 44
    print(calculate_co2_equivalent_weight(sample_mass))