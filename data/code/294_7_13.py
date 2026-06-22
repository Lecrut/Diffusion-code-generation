def calculate_equivalent_weight(mass, molar_mass):
    return mass / molar_mass
if __name__ == '__main__':
    sample_mass = 98
    sample_molar_mass = 98.08
    equivalent_weight = calculate_equivalent_weight(sample_mass, sample_molar_mass)
    print(equivalent_weight)