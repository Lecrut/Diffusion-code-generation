def calculate_equivalent_weight(mass):
    molar_mass_h2o = 18.015
    atomic_mass_o = 16
    return mass / (molar_mass_h2o - atomic_mass_o)

if __name__ == '__main__':
    sample_mass = 18
    print(calculate_equivalent_weight(sample_mass))