def calculate_equivalent_weight(mass_h2, mass_o2):
    molar_mass_h2 = 2.016
    molar_mass_o2 = 32.000
    
    if mass_h2 < 0 or mass_o2 < 0:
        raise ValueError("Masses must be non-negative.")
    
    moles_h2 = mass_h2 / molar_mass_h2
    moles_o2 = mass_o2 / molar_mass_o2
    
    equivalent_weight = (moles_h2 + moles_o2) * (molar_mass_h2 + molar_mass_o2)
    
    return equivalent_weight

if __name__ == '__main__':
    try:
        sample_h2_mass = 2.0
        sample_o2_mass = 32.0
        
        result = calculate_equivalent_weight(sample_h2_mass, sample_o2_mass)
        print(result)
    except ValueError as e:
        print(e)