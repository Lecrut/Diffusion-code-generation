def calculate_equivalent_weight(mass_ammonia, mass_hydrogen):
    molar_mass_ammonia = 17.03
    molar_mass_hydrogen = 1.01
    
    total_molar_mass = molar_mass_ammonia + molar_mass_hydrogen
    
    equivalent_weight_ammonia = (mass_ammonia / molar_mass_ammonia) / (mass_ammonia / molar_mass_ammonia + mass_hydrogen / molar_mass_hydrogen)
    equivalent_weight_hydrogen = (mass_hydrogen / molar_mass_hydrogen) / (mass_ammonia / molar_mass_ammonia + mass_hydrogen / molar_mass_hydrogen)
    
    return equivalent_weight_ammonia, equivalent_weight_hydrogen

if __name__ == '__main__':
    mass_ammonia = 17.0
    mass_hydrogen = 2.0
    equivalent_weights = calculate_equivalent_weight(mass_ammonia, mass_hydrogen)
    print(equivalent_weights)