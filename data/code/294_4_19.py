def calculate_equivalent_weight(mass):
    molar_mass_co2 = 44.01
    return mass / molar_mass_co2

if __name__ == '__main__':
    sample_mass = 44
    equivalent_weight = calculate_equivalent_weight(sample_mass)
    print(equivalent_weight)