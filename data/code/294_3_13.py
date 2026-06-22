def calculate_equivalent_weight(mass_h2, mass_o2):
    molar_mass_h2 = 2.016
    molar_mass_o2 = 32.0
    equivalent_weight_h2 = mass_h2 / molar_mass_h2
    equivalent_weight_o2 = mass_o2 / molar_mass_o2
    total_equivalent_weight = equivalent_weight_h2 + equivalent_weight_o2
    return total_equivalent_weight
if __name__ == '__main__':
    sample_h2_mass = 2.0
    sample_o2_mass = 32.0
    result = calculate_equivalent_weight(sample_h2_mass, sample_o2_mass)
    print(result)