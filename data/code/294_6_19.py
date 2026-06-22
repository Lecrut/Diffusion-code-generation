def calculate_equivalent_weights(mass_nh3, mass_h):
    molar_mass_nh3 = 17.03
    molar_mass_h = 1.01
    total_moles_nh3 = mass_nh3 / molar_mass_nh3
    total_moles_h = mass_h / molar_mass_h
    total_moles = total_moles_nh3 + total_moles_h
    equivalent_weight_nh3 = total_moles_nh3 / total_moles
    equivalent_weight_h = total_moles_h / total_moles
    return (equivalent_weight_nh3, equivalent_weight_h)
if __name__ == '__main__':
    sample_mass_nh3 = 17.0
    sample_mass_h = 2.0
    weights = calculate_equivalent_weights(sample_mass_nh3, sample_mass_h)
    print(weights)