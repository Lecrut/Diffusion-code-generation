MOLAR_MASS_NH3 = 17.03
MOLAR_MASS_H = 1.01

def calculate_equivalent_weights(mass_nh3, mass_h):
    total_mass = mass_nh3 + mass_h
    weight_nh3 = mass_nh3 / total_mass
    weight_h = mass_h / total_mass
    return weight_nh3, weight_h

if __name__ == '__main__':
    sample_mass_nh3 = 17.0
    sample_mass_h = 2.0
    weights = calculate_equivalent_weights(sample_mass_nh3, sample_mass_h)
    print(weights)