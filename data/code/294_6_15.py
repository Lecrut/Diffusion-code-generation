def calculate_equivalent_weights(mass_ammonia, mass_hydrogen):
    molar_mass_ammonia = 17.03
    molar_mass_hydrogen = 1.01
    total_mass = mass_ammonia + mass_hydrogen
    equivalent_weight_ammonia = mass_ammonia / total_mass
    equivalent_weight_hydrogen = mass_hydrogen / total_mass
    return equivalent_weight_ammonia, equivalent_weight_hydrogen

if __name__ == '__main__':
    sample_ammonia_mass = 17.0
    sample_hydrogen_mass = 2.0
    weights = calculate_equivalent_weights(sample_ammonia_mass, sample_hydrogen_mass)
    print(weights)