def calculate_equivalent_weight(mass_ammonia, mass_hydrogen):
    molar_mass_ammonia = 17.03
    molar_mass_hydrogen = 1.01
    
    moles_ammonia = mass_ammonia / molar_mass_ammonia
    moles_hydrogen = mass_hydrogen / molar_mass_hydrogen
    
    equivalent_weight = (moles_ammonia + moles_hydrogen) * molar_mass_ammonia
    
    return equivalent_weight

if __name__ == '__main__':
    sample_mass_ammonia = 17
    sample_mass_hydrogen = 2
    
    result = calculate_equivalent_weight(sample_mass_ammonia, sample_mass_hydrogen)
    
    print(result)